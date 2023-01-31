import { ethers } from 'hardhat'
import { Contract } from 'ethers'
import { expect } from '../../../setup'
import { SignerWithAddress } from '@nomiclabs/hardhat-ethers/signers'

import { deploy } from '../../../helpers'

describe('Changing the owner of L1CrossDomainMessenger', () => {
    let sequencer: SignerWithAddress
    let alice: SignerWithAddress
    let bob: SignerWithAddress
    before(async () => {
        ;[sequencer, alice, bob] = await ethers.getSigners()
    })

    let AddressManager: Contract
    let L1CrossDomainMessenger: Contract
    before(async () => {
        AddressManager = await deploy('Lib_AddressManager')

        const xDomainMessengerImpl = await deploy('L1CrossDomainMessenger')
        await AddressManager.setAddress(
            'L1CrossDomainMessenger',
            xDomainMessengerImpl.address
        )

        const proxy = await deploy('Lib_ResolvedDelegateProxy', {
            args: [AddressManager.address, 'L1CrossDomainMessenger'],
        })
        L1CrossDomainMessenger = xDomainMessengerImpl.attach(proxy.address)

        //print L1CrossDomainMessenger.address
        console.log('L1CrossDomainMessenger.address', L1CrossDomainMessenger.address)

        await L1CrossDomainMessenger.initialize(AddressManager.address)
    })

    it('Changes the owner of the L1CrossDomainMessenger', async () => {
        // Get the current owner
        const currentOwner = await L1CrossDomainMessenger.owner()
        // Change the owner from Alice to Bob
        await L1CrossDomainMessenger.connect(sequencer).transferOwnership(
            bob.address
        )

        // Verify the owner has changed
        const newOwner = await L1CrossDomainMessenger.owner()
        expect(newOwner).to.equal(bob.address)
    })
})
