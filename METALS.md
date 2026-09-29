# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 11:41 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 96 | 94 | 29 (31%) | 39¢ | 47% | -$92.29 | -24% |
| Silver | 49 | 48 | 14 (29%) | 34¢ | 41% | -$29.30 | -17% |
| Gold | 47 | 46 | 15 (33%) | 45¢ | 52% | -$62.99 | -30% |

*Earlier half -$30.35 / later half -$61.94.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 97 | 30 (31%) | -$101.91 | -25% |
| 4¢+ ← live bot | 94 | 31 (33%) | -$37.99 | -11% |
| 6¢+ | 83 | 33 (40%) | $45.27 | +16% |
| 8¢+ | 70 | 29 (41%) | $63.49 | +28% |
| 10¢+ | 58 | 20 (34%) | $19.64 | +11% |
| 15¢+ | 32 | 11 (34%) | $26.53 | +32% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2384 | -2.1% |
| Hyperliquid price vs Kalshi's target | 2384 | +1.8% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 11:32:32 AM | Gold | UP | 12.4 min | 34¢ | 46% | 10¢ | Open | — |
| 9/29 11:32:10 AM | Silver | UP | 12.8 min | 32¢ | 41% | 7¢ | Open | — |
| 9/29 11:19:27 AM | Gold | DOWN | 10.5 min | 35¢ | 41% | 5¢ | ❌ Lost | -$3.66 |
| 9/29 11:16:05 AM | Silver | DOWN | 13.9 min | 41¢ | 48% | 6¢ | ❌ Lost | -$4.27 |
| 9/29 11:01:35 AM | Silver | DOWN | 13.4 min | 36¢ | 44% | 6¢ | ❌ Lost | -$3.77 |
| 9/29 11:01:13 AM | Gold | DOWN | 13.8 min | 45¢ | 52% | 5¢ | ❌ Lost | -$4.68 |
| 9/29 10:50:18 AM | Silver | DOWN | 9.7 min | 29¢ | 36% | 6¢ | ✅ Won | $6.95 |
| 9/29 10:46:06 AM | Gold | UP | 13.9 min | 32¢ | 39% | 6¢ | ❌ Lost | -$3.36 |
| 9/29 10:38:20 AM | Gold | UP | 6.7 min | 48¢ | 55% | 5¢ | ❌ Lost | -$4.98 |
| 9/29 10:37:40 AM | Silver | DOWN | 7.3 min | 17¢ | 26% | 8¢ | ✅ Won | $8.20 |
| 9/29 8:18:54 AM | Silver | DOWN | 11.1 min | 38¢ | 44% | 4¢ | ❌ Lost | -$3.98 |
| 9/29 8:16:12 AM | Gold | DOWN | 13.8 min | 46¢ | 52% | 4¢ | ❌ Lost | -$4.78 |
