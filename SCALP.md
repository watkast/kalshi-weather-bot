# Range-Scalp Bot

*Updated Fri Nov 20 04:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65861 | 57485 | 8376 (124) | 2 | $-17687.11 | -4.3% |
| **+10¢** | 49183 | 39387 | 9796 (165) | 6 | $-16482.54 | -5.3% |
| **+15¢** | 41250 | 30684 | 10566 (211) | 6 | $-14844.80 | -5.7% |
| **+20¢** | 36724 | 25625 | 11099 (267) | 7 | $-13153.58 | -5.7% |
| **+10¢ (15¢ stop)** | 80180 | 80016 | 164 (98) | 3 | $-29529.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 04:55 | +10 stop | BTC | UP | 0.63 | open |  |
| 11-20 04:55 | +15 | BTC | UP | 0.64 | open |  |
| 11-20 04:55 | +10 | BTC | UP | 0.64 | open |  |
| 11-20 04:55 | +5 | BTC | UP | 0.64 | 0.70 | 0.28 |
| 11-20 04:55 | +10 stop | SOL | UP | 0.69 | open |  |
| 11-20 04:55 | +20 | SOL | UP | 0.69 | open |  |
| 11-20 04:55 | +15 | SOL | UP | 0.67 | open |  |
| 11-20 04:55 | +10 | SOL | UP | 0.68 | open |  |
| 11-20 04:55 | +5 | SOL | UP | 0.70 | open |  |
| 11-20 04:55 | +10 stop | NEAR | DOWN | 0.56 | open |  |
| 11-20 04:55 | +20 | NEAR | DOWN | 0.60 | open |  |
| 11-20 04:55 | +15 | NEAR | DOWN | 0.60 | open |  |
| 11-20 04:55 | +10 | NEAR | DOWN | 0.60 | open |  |
| 11-20 04:54 | +10 stop | DOGE | DOWN | 0.50 | 0.22 | -3.08 |
| 11-20 04:54 | +20 | DOGE | DOWN | 0.50 | open |  |
| 11-20 04:54 | +15 | DOGE | DOWN | 0.50 | open |  |
| 11-20 04:54 | +10 | DOGE | DOWN | 0.49 | open |  |
| 11-20 04:54 | +5 | DOGE | DOWN | 0.48 | 0.55 | 0.34 |
| 11-20 04:54 | +10 stop | ETH | UP | 0.67 | 0.81 | 1.13 |
| 11-20 04:54 | +5 | ETH | UP | 0.67 | 0.72 | 0.19 |
| 11-20 04:54 | +5 | XRP | DOWN | 0.40 | 0.59 | 1.56 |
| 11-20 04:53 | +10 stop | XRP | DOWN | 0.64 | 0.42 | -2.55 |
| 11-20 04:53 | +15 | XRP | DOWN | 0.64 | open |  |
| 11-20 04:53 | +10 | XRP | DOWN | 0.64 | open |  |
| 11-20 04:53 | +5 | XRP | DOWN | 0.64 | 0.70 | 0.28 |
| 11-20 04:50 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 11-20 04:50 | +10 stop | NEAR | DOWN | 0.59 | 0.73 | 1.09 |
| 11-20 04:50 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-20 04:49 | +10 stop | ETH | UP | 0.54 | 0.35 | -2.24 |
| 11-20 04:49 | +10 stop | NEAR | UP | 0.71 | 0.54 | -2.03 |
| 11-20 04:48 | +5 | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-20 04:48 | +10 stop | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 11-20 04:48 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-20 04:48 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 11-20 04:48 | +10 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 11-20 04:48 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 11-20 04:48 | +5 | NEAR | UP | 0.69 | open |  |
| 11-20 04:48 | +10 stop | DOGE | DOWN | 0.60 | 0.74 | 1.09 |
| 11-20 04:48 | +20 | DOGE | DOWN | 0.60 | 0.82 | 1.92 |
| 11-20 04:48 | +15 | DOGE | DOWN | 0.60 | 0.82 | 1.92 |
