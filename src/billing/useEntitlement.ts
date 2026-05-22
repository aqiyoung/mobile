import { useMemo } from 'react';

import { computeEntitlement, type Entitlement } from './entitlement';

export function useEntitlement(): Entitlement {
  return useMemo(() => computeEntitlement(), []);
}
