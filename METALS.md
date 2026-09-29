# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 7:50 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

⏳ **Too early.** 4 of 30 settled trades needed before judging.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 6 | 4 | 3 (75%) | 36¢ | 45% | $15.15 | +102% |
| Silver | 3 | 2 | 1 (50%) | 31¢ | 41% | $3.49 | +54% |
| Gold | 3 | 2 | 2 (100%) | 40¢ | 49% | $11.66 | +140% |

*Earlier half $2.27 / later half $12.88.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 4 | 3 (75%) | $14.44 | +93% |
| 4¢+ ← live bot | 4 | 3 (75%) | $18.01 | +150% |
| 6¢+ | 4 | 3 (75%) | $19.26 | +179% |
| 8¢+ | 4 | 3 (75%) | $21.38 | +248% |
| 10¢+ | 3 | 1 (33%) | $5.13 | +105% |
| 15¢+ | 1 | 1 (100%) | $9.02 | +920% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 96 | +9.6% |
| Hyperliquid price vs Kalshi's target | 96 | +24.5% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 7:47:42 PM | Silver | UP | 12.3 min | 30¢ | 37% | 5¢ | Open | — |
| 9/28 7:46:12 PM | Gold | DOWN | 13.8 min | 44¢ | 51% | 5¢ | Open | — |
| 9/28 7:32:13 PM | Silver | UP | 12.8 min | 33¢ | 41% | 6¢ | ✅ Won | $6.54 |
| 9/28 7:31:57 PM | Gold | UP | 13.1 min | 35¢ | 45% | 8¢ | ✅ Won | $6.34 |
| 9/28 7:17:04 PM | Gold | UP | 12.9 min | 45¢ | 54% | 7¢ | ✅ Won | $5.32 |
| 9/28 7:17:00 PM | Silver | UP | 13.0 min | 29¢ | 41% | 11¢ | ❌ Lost | -$3.05 |
