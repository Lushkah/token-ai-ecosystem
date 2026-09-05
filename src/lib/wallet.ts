import "react-native-get-random-values";
import * as SecureStore from "expo-secure-store";
import { Wallet } from "ethers";
const KEY="lushka.wallet.privateKey";
export async function createWallet(){const w=Wallet.createRandom(); await SecureStore.setItemAsync(KEY,w.privateKey,{keychainAccessible:SecureStore.WHEN_UNLOCKED_THIS_DEVICE_ONLY}); return {address:w.address,privateKey:w.privateKey};}
export async function importWallet(privateKey:string){const w=new Wallet(privateKey.trim()); await SecureStore.setItemAsync(KEY,w.privateKey,{keychainAccessible:SecureStore.WHEN_UNLOCKED_THIS_DEVICE_ONLY}); return {address:w.address};}
export async function getWallet(){const pk=await SecureStore.getItemAsync(KEY); if(!pk)return null; const w=new Wallet(pk); return {address:w.address,privateKey:pk};}
export async function clearWallet(){await SecureStore.deleteItemAsync(KEY);}
