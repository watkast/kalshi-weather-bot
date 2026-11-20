# Range-Scalp Bot

*Updated Fri Nov 20 00:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65520 | 57195 | 8325 (124) | 1 | $-17531.56 | -4.3% |
| **+10¢** | 48931 | 39196 | 9735 (165) | 2 | $-16305.67 | -5.3% |
| **+15¢** | 41034 | 30533 | 10501 (211) | 5 | $-14671.04 | -5.7% |
| **+20¢** | 36535 | 25502 | 11033 (266) | 4 | $-12994.93 | -5.7% |
| **+10¢ (15¢ stop)** | 79764 | 79600 | 164 (98) | 2 | $-29340.88 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 00:22 | +10 stop | NEAR | DOWN | 0.59 | open |  |
| 11-20 00:21 | +10 stop | ETH | UP | 0.65 | 0.77 | 0.91 |
| 11-20 00:21 | +10 | ETH | UP | 0.65 | 0.77 | 0.91 |
| 11-20 00:21 | +5 | ETH | UP | 0.63 | 0.72 | 0.58 |
| 11-20 00:20 | +10 stop | SOL | UP | 0.65 | 0.75 | 0.70 |
| 11-20 00:20 | +15 | SOL | UP | 0.64 | open |  |
| 11-20 00:20 | +10 | SOL | UP | 0.65 | 0.75 | 0.70 |
| 11-20 00:20 | +5 | SOL | UP | 0.65 | 0.70 | 0.19 |
| 11-20 00:19 | +10 stop | ZEC | UP | 0.58 | open |  |
| 11-20 00:19 | +10 stop | DOGE | UP | 0.69 | 0.81 | 0.94 |
| 11-20 00:19 | +15 | DOGE | UP | 0.69 | open |  |
| 11-20 00:19 | +10 | DOGE | UP | 0.69 | 0.81 | 0.94 |
| 11-20 00:19 | +5 | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 11-20 00:18 | +10 stop | NEAR | UP | 0.60 | 0.38 | -2.51 |
| 11-20 00:17 | +10 stop | ZEC | UP | 0.67 | 0.50 | -2.04 |
| 11-20 00:17 | +20 | ZEC | UP | 0.67 | open |  |
| 11-20 00:17 | +15 | ZEC | UP | 0.67 | open |  |
| 11-20 00:17 | +10 | ZEC | UP | 0.67 | open |  |
| 11-20 00:17 | +5 | ZEC | UP | 0.67 | open |  |
| 11-20 00:16 | +10 stop | NEAR | DOWN | 0.57 | 0.38 | -2.25 |
| 11-20 00:16 | +20 | NEAR | DOWN | 0.57 | open |  |
| 11-20 00:16 | +15 | NEAR | DOWN | 0.57 | open |  |
| 11-20 00:16 | +10 | NEAR | DOWN | 0.57 | open |  |
| 11-20 00:16 | +5 | NEAR | DOWN | 0.57 | 0.65 | 0.46 |
| 11-20 00:16 | +5 | HYPE | UP | 0.68 | 0.78 | 0.71 |
| 11-20 00:16 | +10 stop | XRP | UP | 0.62 | 0.75 | 0.99 |
| 11-20 00:16 | +20 | XRP | UP | 0.62 | 0.82 | 1.72 |
| 11-20 00:16 | +15 | XRP | UP | 0.62 | 0.78 | 1.30 |
| 11-20 00:16 | +10 | XRP | UP | 0.62 | 0.75 | 0.99 |
| 11-20 00:16 | +5 | XRP | UP | 0.62 | 0.67 | 0.17 |
| 11-20 00:16 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-20 00:16 | +20 | ETH | UP | 0.69 | open |  |
| 11-20 00:16 | +15 | ETH | UP | 0.69 | open |  |
| 11-20 00:16 | +10 | ETH | UP | 0.69 | 0.80 | 0.83 |
| 11-20 00:16 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 11-20 00:16 | +10 stop | DOGE | UP | 0.57 | 0.70 | 0.97 |
| 11-20 00:16 | +20 | DOGE | UP | 0.57 | 0.81 | 2.11 |
| 11-20 00:16 | +15 | DOGE | UP | 0.57 | 0.74 | 1.38 |
| 11-20 00:16 | +10 | DOGE | UP | 0.57 | 0.70 | 0.97 |
| 11-20 00:16 | +5 | DOGE | UP | 0.57 | 0.63 | 0.25 |
