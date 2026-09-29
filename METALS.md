# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 3:32 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 50 | 48 | 16 (33%) | 39¢ | 47% | -$36.13 | -18% |
| Silver | 25 | 24 | 7 (29%) | 34¢ | 43% | -$16.20 | -19% |
| Gold | 25 | 24 | 9 (38%) | 44¢ | 52% | -$19.93 | -18% |

*Earlier half $16.31 / later half -$52.44.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 49 | 13 (27%) | -$74.08 | -36% |
| 4¢+ ← live bot | 47 | 14 (30%) | -$33.89 | -19% |
| 6¢+ | 43 | 14 (33%) | $0.13 | +0% |
| 8¢+ | 38 | 12 (32%) | $11.35 | +10% |
| 10¢+ | 31 | 8 (26%) | $1.75 | +2% |
| 15¢+ | 16 | 5 (31%) | $15.52 | +45% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1205 | -6.7% |
| Hyperliquid price vs Kalshi's target | 1205 | -10.7% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:32:14 AM | Silver | DOWN | 12.8 min | 35¢ | 41% | 4¢ | Open | — |
| 9/29 3:31:07 AM | Gold | DOWN | 13.9 min | 47¢ | 56% | 7¢ | Open | — |
| 9/29 3:22:33 AM | Silver | UP | 7.5 min | 56¢ | 66% | 8¢ | ❌ Lost | -$5.78 |
| 9/29 3:16:18 AM | Gold | DOWN | 13.7 min | 39¢ | 50% | 9¢ | ❌ Lost | -$4.07 |
| 9/29 3:04:34 AM | Silver | DOWN | 10.4 min | 32¢ | 40% | 7¢ | ✅ Won | $6.64 |
| 9/29 3:02:03 AM | Gold | DOWN | 12.9 min | 31¢ | 38% | 6¢ | ❌ Lost | -$3.25 |
| 9/29 12:33:04 AM | Gold | DOWN | 11.9 min | 33¢ | 42% | 7¢ | ❌ Lost | -$3.46 |
| 9/29 12:31:29 AM | Silver | DOWN | 13.5 min | 34¢ | 40% | 4¢ | ❌ Lost | -$3.56 |
| 9/29 12:16:42 AM | Silver | UP | 13.3 min | 28¢ | 35% | 5¢ | ❌ Lost | -$2.95 |
| 9/29 12:16:24 AM | Gold | UP | 13.6 min | 28¢ | 37% | 8¢ | ❌ Lost | -$2.95 |
| 9/29 12:03:03 AM | Gold | DOWN | 11.9 min | 36¢ | 45% | 7¢ | ❌ Lost | -$3.77 |
| 9/29 12:03:03 AM | Silver | DOWN | 11.9 min | 12¢ | 18% | 5¢ | ❌ Lost | -$1.28 |
