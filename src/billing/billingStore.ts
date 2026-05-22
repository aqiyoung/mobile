import { create } from 'zustand';

type State = {
  ready: boolean;
  purchased: boolean;
};

type Actions = {
  init: () => Promise<void>;
  refresh: () => Promise<void>;
};

export type BillingStore = State & Actions;

export const useBillingStore = create<BillingStore>()((set) => ({
  ready: true,
  purchased: true,

  init: async () => {
    set({ ready: true, purchased: true });
  },

  refresh: async () => {
    set({ purchased: true });
  },
}));
