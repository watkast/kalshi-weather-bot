# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 7:39 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

⏳ **Too early.** 2 of 30 settled trades needed before judging.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 4 | 2 | 1 (50%) | 37¢ | 48% | $2.27 | +29% |
| Silver | 2 | 1 | 0 (0%) | 29¢ | 41% | -$3.05 | -100% |
| Gold | 2 | 1 | 1 (100%) | 45¢ | 54% | $5.32 | +114% |

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 2 | 1 (50%) | $3.19 | +47% |
| 4¢+ ← live bot | 2 | 1 (50%) | $4.42 | +79% |
| 6¢+ | 2 | 1 (50%) | $3.80 | +61% |
| 8¢+ | 2 | 1 (50%) | $5.92 | +145% |
| 10¢+ | 2 | 0 (0%) | -$4.12 | -100% |
| 15¢+ | 0 | — | — | — |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 46 | -18.9% |
| Hyperliquid price vs Kalshi's target | 46 | -2.7% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 7:32:13 PM | Silver | UP | 12.8 min | 33¢ | 41% | 6¢ | Open | — |
| 9/28 7:31:57 PM | Gold | UP | 13.1 min | 35¢ | 45% | 8¢ | Open | — |
| 9/28 7:17:04 PM | Gold | UP | 12.9 min | 45¢ | 54% | 7¢ | ✅ Won | $5.32 |
| 9/28 7:17:00 PM | Silver | UP | 13.0 min | 29¢ | 41% | 11¢ | ❌ Lost | -$3.05 |
