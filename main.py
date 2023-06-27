import asyncio
import json
import random
import time

from web3 import AsyncWeb3
from web3.providers.async_rpc import AsyncHTTPProvider


with open('proxy_erc20abi.json') as f:
    proxy_erc20abi = json.load(f)
with open('proxy_hrc20abi.json') as f:
    proxy_hrc20abi = json.load(f)
with open('usdt_abi.json') as f:
    usdt_abi = json.load(f)
with open('usdc_abi.json') as f:
    usdc_abi = json.load(f)
with open('usdt_hrc20abi.json') as f:
    usdt_hrc20_abi = json.load(f)
with open('usdc_hrc20abi.json') as f:
    usdc_hrc20_abi = json.load(f)
with open('sushiswap_abi.json') as f:
    sushiswap_abi = json.load(f)


class Arbitrum:

    def __init__(self):
        self.id = 110
        self.w3 = AsyncWeb3(AsyncHTTPProvider('https://endpoints.omniatech.io/v1/arbitrum/one/public'))

        self.proxy_usdc_address = self.w3.to_checksum_address('0x1c3979C2bb4f0e6dcb75Daf22ad0741Cf7D5F160')
        self.proxy_usdc_contract = self.w3.eth.contract(address=self.proxy_usdc_address, abi=proxy_erc20abi)

        self.proxy_usdt_address = self.w3.to_checksum_address('0x297f0b9A452D34c9b1C15B36B173a9A0B0F0E10b')
        self.proxy_usdt_contract = self.w3.eth.contract(address=self.proxy_usdt_address, abi=proxy_erc20abi)

        self.usdt_address = self.w3.to_checksum_address('0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9')
        self.usdt_contract = self.w3.eth.contract(address=self.usdt_address, abi=usdt_abi)

        self.usdc_address = self.w3.to_checksum_address('0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8')
        self.usdc_contract = self.w3.eth.contract(address=self.usdc_address, abi=usdc_abi)

        self.blockExplorerUrl = 'https://arbiscan.io'
        self.native_token = 'ETH'
        self.native_token_address = self.w3.to_checksum_address('0x82aF49447D8a07e3bd95BD0d56f35241523fBab1')

        self.sushiswap_address = self.w3.to_checksum_address('0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506')
        self.sushiswap_contract = self.w3.eth.contract(address=self.sushiswap_address, abi=sushiswap_abi)


class BinanceSmartChain:

    def __init__(self):
        self.id = 102
        self.w3 = AsyncWeb3(AsyncHTTPProvider('https://rpc.ankr.com/bsc'))

        self.proxy_usdt_address = self.w3.to_checksum_address('0x0551Ca9E33bada0355Dfce34685Ad3B73CF3Ad70')
        self.proxy_usdt_contract = self.w3.eth.contract(address=self.proxy_usdt_address, abi=proxy_erc20abi)

        self.proxy_usdc_address = self.w3.to_checksum_address('0x8d1ebcda83fd905b597bf6d3294766b64ecf2aa7')
        self.proxy_usdc_contract = self.w3.eth.contract(address=self.proxy_usdc_address, abi=proxy_erc20abi)

        self.usdt_address = self.w3.to_checksum_address('0x55d398326f99059fF775485246999027B3197955')
        self.usdt_contract = self.w3.eth.contract(address=self.usdt_address, abi=usdt_abi)

        self.usdc_address = self.w3.to_checksum_address('0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d')
        self.usdc_contract = self.w3.eth.contract(address=self.usdc_address, abi=usdc_abi)

        self.blockExplorerUrl = 'https://bscscan.com'
        self.native_token = 'BNB'
        self.native_token_address = self.w3.to_checksum_address('0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c')

        self.sushiswap_address = self.w3.to_checksum_address('0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506')
        self.sushiswap_contract = self.w3.eth.contract(address=self.sushiswap_address, abi=sushiswap_abi)


class Harmony:

    def __init__(self):
        self.id = 116
        self.w3 = AsyncWeb3(AsyncHTTPProvider('https://api.harmony.one'))

        self.arbUSDC_proxy_address = self.w3.to_checksum_address('0x11C4E687b865c1E8e17437748Ab3D1faed7444ff')
        self.arbUSDC_proxy_contract = self.w3.eth.contract(address=self.arbUSDC_proxy_address, abi=proxy_hrc20abi)

        self.arbUSDT_proxy_address = self.w3.to_checksum_address('0xe7cF1A353cDd4fb8cC8dF4E80B2F7D27552CA711')
        self.arbUSDT_proxy_contract = self.w3.eth.contract(address=self.arbUSDT_proxy_address, abi=proxy_hrc20abi)

        self.bscUSDC_proxy_address = self.w3.to_checksum_address('0xcE59e51645De8F8FF24229F89e105CadEb96EA57')
        self.bscUSDC_proxy_contract = self.w3.eth.contract(address=self.bscUSDC_proxy_address, abi=proxy_hrc20abi)

        self.bscUSDT_proxy_address = self.w3.to_checksum_address('0x8bab2DDe26CE3f948b9B3E146760B66b60810fc7')
        self.bscUSDT_proxy_contract = self.w3.eth.contract(address=self.bscUSDT_proxy_address, abi=proxy_hrc20abi)

        self.arbUSDC_address = self.w3.to_checksum_address('0x9b5fae311A4A4b9d838f301C9c27b55d19BAa4Fb')
        self.arbUSDC_contract = self.w3.eth.contract(address=self.arbUSDC_address, abi=usdc_hrc20_abi)

        self.arbUSDT_address = self.w3.to_checksum_address('0x2DA729BA5231d2C79290aBA4a8b85a5c94dA4724')
        self.arbUSDT_contract = self.w3.eth.contract(address=self.arbUSDT_address, abi=usdt_hrc20_abi)

        self.bscUSDC_address = self.w3.to_checksum_address('0x44cED87b9F1492Bf2DCf5c16004832569f7f6cBa')
        self.bscUSDC_contract = self.w3.eth.contract(address=self.bscUSDC_address, abi=usdc_abi)

        self.bscUSDT_address = self.w3.to_checksum_address('0x9A89d0e1b051640C6704Dde4dF881f73ADFEf39a')
        self.bscUSDT_contract = self.w3.eth.contract(address=self.bscUSDT_address, abi=usdt_abi)

        self.blockExplorerUrl = 'https://explorer.harmony.one'


arb = Arbitrum()
bsc = BinanceSmartChain()
hmy = Harmony()


async def swap_usdt(chain_from, chain_to, wallet):
    account = chain_from.w3.eth.account.from_key(wallet)
    address = account.address

    if chain_from.__class__.__name__ == 'Harmony':
        if chain_to.__class__.__name__ == 'Arbitrum':
            proxy_contract = chain_from.arbUSDT_proxy_contract
            proxy_address = chain_from.arbUSDT_proxy_address
            usdt_contract = chain_from.arbUSDT_contract

        elif chain_to.__class__.__name__ == 'BinanceSmartChain':
            proxy_contract = chain_from.bscUSDT_proxy_contract
            proxy_address = chain_from.bscUSDT_proxy_address
            usdt_contract = chain_from.bscUSDT_contract
        else:
            proxy_contract = chain_from.proxy_usdt_contract
            proxy_address = chain_from.proxy_usdt_address
            usdt_contract = chain_from.usdt_contract
    else:
        proxy_contract = chain_from.proxy_usdt_contract
        proxy_address = chain_from.proxy_usdt_address
        usdt_contract = chain_from.usdt_contract

    usdt_balance = await check_balance(address, usdt_contract)

    adapterParams = '0x0001000000000000000000000000000000000000000000000000000000000007a120'

    fees = await proxy_contract.functions.estimateSendFee(chain_to.id, address, usdt_balance, False,
                                                          adapterParams).call()
    fee = fees[0]
    allowance = await usdt_contract.functions.allowance(address, proxy_address).call()

    if allowance < usdt_balance:
        max_amount = chain_from.w3.to_wei(2 ** 64 - 1, 'ether')
        gas_price = await chain_from.w3.eth.gas_price
        nonce = await chain_from.w3.eth.get_transaction_count(address)
        approve_txn = await usdt_contract.functions.approve(proxy_address, max_amount).build_transaction({
            'from': address,
            'gasPrice': int(gas_price / 3),
            'nonce': nonce,
        })
        
        gas_estimate = await chain_from.w3.eth.estimate_gas(approve_txn)
        approve_txn['gas'] = gas_estimate
        try:
            signed_approve_txn = chain_from.w3.eth.account.sign_transaction(approve_txn, wallet)
            approve_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)
            print(
                f"{chain_from.__class__.__name__} | USDT APPROVED {chain_from.blockExplorerUrl}/tx/{approve_txn_hash.hex()}")
        
            await asyncio.sleep(50)
        except Exception as e:
            print(e)
            print(address)
    else:
        pass

    amount = [10000000000000000, 20000000000000000]

    _from = address
    _chainId = chain_to.id
    _toaddress = address
    _tokenId = int(random.sample(amount, 1)[0])
    _zropayment = '0x0000000000000000000000000000000000000000'
    _refund_address = address

    if chain_from.__class__.__name__ == 'Harmony':
        _adapter_params = b''
    elif chain_from.__class__.__name__ == 'Arbitrum':
        _adapter_params = b''
    else:
        _adapter_params = '0x0001000000000000000000000000000000000000000000000000000000000007a120'

    gas_price = await chain_from.w3.eth.gas_price
    nonce = await chain_from.w3.eth.get_transaction_count(address)
    swap_txn = await proxy_contract.functions.sendFrom(
        _from, _chainId, _toaddress, _tokenId, _refund_address, _zropayment, _adapter_params
    ).build_transaction({
        'from': address,
        'value': fee,
        'gasPrice': int(gas_price / 3),
        'nonce': nonce,
    })
    gas_estimate = await chain_from.w3.eth.estimate_gas(swap_txn)
    swap_txn['gas'] = gas_estimate
    
    try:
        signed_swap_txn = chain_from.w3.eth.account.sign_transaction(swap_txn, wallet)
        swap_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)
        return swap_txn_hash

    except Exception as e:
        print(e)
        print(address)


async def swap_usdc(chain_from, chain_to, wallet):

    account = chain_from.w3.eth.account.from_key(wallet)
    address = account.address


    if chain_from.__class__.__name__ == 'Harmony':
        if chain_to.__class__.__name__ == 'Arbitrum':
            proxy_contract = chain_from.arbUSDC_proxy_contract
            proxy_address = chain_from.arbUSDC_proxy_address
            usdc_contract = chain_from.arbUSDC_contract

        elif chain_to.__class__.__name__ == 'BinanceSmartChain':
            proxy_contract = chain_from.bscUSDC_proxy_contract
            proxy_address = chain_from.bscUSDC_proxy_address
            usdc_contract = chain_from.bscUSDC_contract
        else:
            proxy_contract = chain_from.proxy_usdc_contract
            proxy_address = chain_from.proxy_usdc_address
            usdc_contract = chain_from.usdc_contract
    else:
        proxy_contract = chain_from.proxy_usdc_contract
        proxy_address = chain_from.proxy_usdc_address
        usdc_contract = chain_from.usdc_contract

    usdc_balance = await check_balance(address, usdc_contract)

    adapterParams = '0x0001000000000000000000000000000000000000000000000000000000000007a120'

    fees = await proxy_contract.functions.estimateSendFee(chain_to.id, address, usdc_balance, False,
                                                          adapterParams).call()
    fee = fees[0]
    allowance = await usdc_contract.functions.allowance(address, proxy_address).call()

    if allowance < usdc_balance:
        
        max_amount = chain_from.w3.to_wei(2 ** 64 - 1, 'ether')
        gas_price = await chain_from.w3.eth.gas_price
        nonce = await chain_from.w3.eth.get_transaction_count(address)    
        approve_txn = await usdc_contract.functions.approve(proxy_address, max_amount).build_transaction({
            'from': address,
            'gasPrice': int(gas_price / 3),
            'nonce': nonce,
        })

        gas_estimate = await chain_from.w3.eth.estimate_gas(approve_txn)
        approve_txn['gas'] = gas_estimate
        try:
            signed_approve_txn = chain_from.w3.eth.account.sign_transaction(approve_txn, wallet)
            approve_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)
            print(
                f"{chain_from.__class__.__name__} | USDС APPROVED {chain_from.blockExplorerUrl}/tx/{approve_txn_hash.hex()}")
            await asyncio.sleep(50)
        except Exception as e:
            print(e)
            print(address)

    amount = [10000000000000000, 20000000000000000]

    _from = address
    _chainId = chain_to.id
    _toaddress = address
    _tokenId = int(random.sample(amount, 1)[0])
    _zropayment = '0x0000000000000000000000000000000000000000'
    _refund_address = address

    if chain_from.__class__.__name__ == 'Harmony':
        _adapter_params = b''
    elif chain_from.__class__.__name__ == 'Arbitrum':
        _adapter_params = b''
    else:
        _adapter_params = '0x0001000000000000000000000000000000000000000000000000000000000007a120'

    gas_price = await chain_from.w3.eth.gas_price
    nonce = await chain_from.w3.eth.get_transaction_count(address)    
    swap_txn = await proxy_contract.functions.sendFrom(
        _from, _chainId, _toaddress, _tokenId, _refund_address, _zropayment, _adapter_params
    ).build_transaction({
        'from': address,
        'value': fee,
        'gasPrice': int(gas_price / 3),
        'nonce': nonce,
    })
    gas_estimate = await chain_from.w3.eth.estimate_gas(swap_txn)
    swap_txn['gas'] = gas_estimate
    
    try:
        signed_swap_txn = chain_from.w3.eth.account.sign_transaction(swap_txn, wallet)
        swap_txn_hash = await chain_from.w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)
        return swap_txn_hash

    except Exception as e:
        print(e)
        print(address)


async def get_amount_out(chain, amountIn, tokenIn, tokenOut):
    try:
        contract_txn = await chain.sushiswap_contract.functions.getAmountsOut(
            amountIn,
            [tokenIn, tokenOut],
        ).call()

        amountsOut = contract_txn[1]

        return int(amountsOut * 0.99)
    
    except Exception as e:
        print(e)


async def sushiswap_native(wallet, chain, token):

    account = chain.w3.eth.account.from_key(wallet)
    address = account.address
    #balance = await chain.w3.eth.get_balance(address)
    #keep_value = balance / 2
    #amount_for_usdt = (balance - keep_value) / 2

    amount = random.randint(1000000000000000,1300000000000000)

    tokenIn = chain.native_token_address
    amountIn = int(amount)
    tokenOut = chain.usdt_address if token == 'USDT' else chain.usdc_address
    amountOut = await get_amount_out(chain, amountIn, tokenIn, tokenOut)

    nonce = await chain.w3.eth.get_transaction_count(address)
    gas_price = await chain.w3.eth.gas_price

    txn = await chain.sushiswap_contract.functions.swapExactETHForTokens(
        amountOut,
        [tokenIn, tokenOut],
        address,
        (int(time.time()) + 10000)
    ).build_transaction(
        {
            "from": address,
            "value": amountIn,
            "nonce": nonce,
            'gasPrice': int(gas_price / 3),
        }
    )

    gas_estimate = await chain.w3.eth.estimate_gas(txn)
    txn["gas"] = gas_estimate
    try:
        signed_txn = chain.w3.eth.account.sign_transaction(txn, wallet)
        txn_hash = await chain.w3.eth.send_raw_transaction(signed_txn.rawTransaction)

        print(
            f"{chain.__class__.__name__}| BUY {token} | {address} | Transaction: {chain.blockExplorerUrl}/tx/{txn_hash.hex()}")

        await asyncio.sleep(50)
    except Exception as e:
        print(e)


async def check_allowance(chain, wallet, balance, contract):

    account = chain.w3.eth.account.from_key(wallet)
    address = account.address

    allowance = await contract.functions.allowance(address, chain.sushiswap_address).call()

    nonce = await chain.w3.eth.get_transaction_count(address)
    gas_price = await chain.w3.eth.gas_price
    if chain.__class__.__name__ == 'Arbitrum':
        gas = 1000000
    else:
        gas = 500000

    if allowance < balance:
        max_amount = chain.w3.to_wei(2 ** 64 - 1, 'ether')
        approve_txn = await contract.functions.approve(chain.sushiswap_address,
                                                       max_amount).build_transaction({
            'from': address,
            'gas': gas,
            'gasPrice': int(gas_price / 2),
            'nonce': nonce
        })
        signed_approve_txn = chain.w3.eth.account.sign_transaction(approve_txn, wallet)
        approve_txn_hash = await chain.w3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)
        print(
            f"{chain.__class__.__name__} | TOKEN APPROVED {chain.blockExplorerUrl}/tx/{approve_txn_hash.hex()}")
    else:
        return


async def sushiswap_token(wallet, chain, token):
    try:
        account = chain.w3.eth.account.from_key(wallet)
        address = account.address
        balance = await check_balance(address, chain.usdt_contract) if token == 'USDT' else await check_balance(address,
                                                                                                                chain.usdc_contract)
        tokenIn = chain.usdt_address if token == 'USDT' else chain.usdc_address
        amountIn = int(balance)
        tokenOut = chain.native_token_address
        amountOut = await get_amount_out(chain, amountIn, tokenIn, tokenOut)

        allowance = await check_allowance(chain, wallet, balance, chain.usdt_contract) if token == 'USDT' else await check_allowance(chain, wallet, balance, chain.usdc_contract)
        await asyncio.sleep(20)

        nonce = await chain.w3.eth.get_transaction_count(address)
        gas_price = await chain.w3.eth.gas_price

        txn = await chain.sushiswap_contract.functions.swapExactTokensForETH(
            amountIn,
            amountOut,
            [tokenIn, tokenOut],
            address,
            (int(time.time()) + 10000)
        ).build_transaction(
            {
                "from": address,
                "value": 0,
                "nonce": nonce,
                'gasPrice': gas_price,
            }
        )

        gas_estimate = await chain.w3.eth.estimate_gas(txn)
        txn["gas"] = gas_estimate
        signed_txn = chain.w3.eth.account.sign_transaction(txn, wallet)
        txn_hash = await chain.w3.eth.send_raw_transaction(signed_txn.rawTransaction)

        print(
            f"{chain.__class__.__name__}| SELL {token} | {address} | Transaction: {chain.blockExplorerUrl}/tx/{txn_hash.hex()}")
        await asyncio.sleep(15)
    except Exception as e:
        print(e)



async def check_balance(address, contract):
    balance = await contract.functions.balanceOf(address).call()
    return balance


async def work(wallet):
    start_delay = random.randint(10, 1000)
    await asyncio.sleep(start_delay)

    address = bsc.w3.eth.account.from_key(wallet).address
    try:
        await sushiswap_native(wallet, bsc, 'USDT')
        await asyncio.sleep(30)
        await sushiswap_native(wallet, bsc, 'USDC')
        await asyncio.sleep(30)
    except Exception as e:
        print(e)
        print(address)
    # await sushiswap_native(wallet, arb, 'USDT')
    # await asyncio.sleep(30)
    # await sushiswap_native(wallet, arb, 'USDC')
    # await asyncio.sleep(30)

    chains = [
         (bsc, hmy, bsc.usdc_contract, swap_usdc, "USDC", "BSC", "Harmony"),
         (bsc, hmy, bsc.usdt_contract, swap_usdt, "USDT", "BSC", "Harmony"),
         (bsc, hmy, bsc.usdc_contract, swap_usdc, "USDC", "BSC", "Harmony"),
         (bsc, hmy, bsc.usdt_contract, swap_usdt, "USDT", "BSC", "Harmony"),
         # (bsc, hmy, bsc.usdc_contract, swap_usdc, "USDC", "BSC", "Harmony"),
         # (bsc, hmy, bsc.usdt_contract, swap_usdt, "USDT", "BSC", "Harmony"),
         # (bsc, hmy, bsc.usdc_contract, swap_usdc, "USDC", "BSC", "Harmony"),
         # (bsc, hmy, bsc.usdt_contract, swap_usdt, "USDT", "BSC", "Harmony"),
         # (bsc, hmy, bsc.usdc_contract, swap_usdc, "USDC", "BSC", "Harmony"),
         # (bsc, hmy, bsc.usdt_contract, swap_usdt, "USDT", "BSC", "Harmony"),
         # (bsc, hmy, bsc.usdc_contract, swap_usdc, "USDC", "BSC", "Harmony"),
         # (bsc, hmy, bsc.usdt_contract, swap_usdt, "USDT", "BSC", "Harmony"),
        # (arb, hmy, arb.usdt_contract, swap_usdt, "USDT", "Arbitrum", "Harmony"),
        # (arb, hmy, arb.usdc_contract, swap_usdc, "USDC", "Arbitrum", "Harmony"),
        # (hmy, bsc, hmy.bscUSDC_contract, swap_usdc, "USDС", "Harmony", "BSC"),
        # (hmy, bsc, hmy.bscUSDT_contract, swap_usdt, "USDT", "Harmony", "BSC"),
        # (hmy, arb, hmy.arbUSDC_contract, swap_usdc, "USDС", "Harmony", "Arbitrum"),
        # (hmy, arb, hmy.arbUSDT_contract, swap_usdt, "USDT", "Harmony", "Arbitrum")
    ]

    for (from_chain, to_chain, contract, swap_fn, token, from_name, to_name) in chains:

        #balance = await check_balance(address, contract)

        # while balance < 100000:
        #     await asyncio.sleep(60)
        #     balance = await check_balance(address, contract)
        #
        txn_hash = await swap_fn(from_chain, to_chain, wallet)
        print(f"{from_name} -> {to_name} | {token} | {address} | Transaction: {from_chain.blockExplorerUrl}/tx/{txn_hash.hex()}")
        
        await asyncio.sleep(300)

    # await asyncio.sleep(30)
    # await sushiswap_token(wallet, bsc, 'USDT')
    # await asyncio.sleep(15)
    # await sushiswap_token(wallet, bsc, 'USDC')
    # await asyncio.sleep(15)
    # await sushiswap_token(wallet, arb, 'USDT')
    # await asyncio.sleep(15)
    # await sushiswap_token(wallet, arb, 'USDC')
    # await asyncio.sleep(15)
    
    print(f'Wallet: {address} | DONE')


async def main():
    with open('wallets.txt', 'r') as f:
        WALLETS = [row.strip() for row in f]

    await asyncio.sleep(10)

    tasks = []
    for wallet in WALLETS:
        tasks.append(asyncio.create_task(work(wallet)))

    for task in tasks:
        await task

    await asyncio.sleep(10)

    print(f'*** ALL JOB IS DONE ***')


if __name__ == '__main__':
    asyncio.run(main())
