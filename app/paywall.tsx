import { Redirect } from 'expo-router';
import { Platform } from 'react-native';

import { PaywallScreen } from '@/components/billing/PaywallScreen';

export default function Paywall() {
  if (Platform.OS === 'ios') return <Redirect href="/" />;
  return <PaywallScreen />;
}
