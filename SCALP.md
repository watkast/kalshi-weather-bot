# Range-Scalp Bot

*Updated Sat Nov 07 03:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50409 | 43936 | 6473 (76) | 1 | $-14203.33 | -4.5% |
| **+10¢** | 37622 | 30086 | 7536 (102) | 1 | $-13134.35 | -5.6% |
| **+15¢** | 31506 | 23383 | 8123 (131) | 1 | $-12073.40 | -6.1% |
| **+20¢** | 28011 | 19496 | 8515 (173) | 1 | $-10673.47 | -6.1% |
| **+10¢ (15¢ stop)** | 61375 | 61276 | 99 (58) | 1 | $-22723.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 03:48 | +5 | ZEC | UP | 0.69 | open |  |
| 11-07 03:46 | +10 stop | ZEC | UP | 0.64 | open |  |
| 11-07 03:46 | +20 | ZEC | UP | 0.64 | open |  |
| 11-07 03:46 | +15 | ZEC | UP | 0.64 | open |  |
| 11-07 03:46 | +10 | ZEC | UP | 0.64 | open |  |
| 11-07 03:46 | +5 | ZEC | UP | 0.63 | 0.68 | 0.17 |
| 11-07 03:32 | +10 stop | BNB | UP | 0.45 | 0.26 | -2.22 |
| 11-07 03:32 | +10 stop | ETH | DOWN | 0.68 | 0.85 | 1.45 |
| 11-07 03:32 | +10 stop | ZEC | DOWN | 0.64 | 0.80 | 1.31 |
| 11-07 03:32 | +10 | ZEC | DOWN | 0.64 | 0.80 | 1.31 |
| 11-07 03:32 | +5 | ZEC | DOWN | 0.64 | 0.69 | 0.18 |
| 11-07 03:32 | +15 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 11-07 03:32 | +10 stop | SOL | DOWN | 0.69 | 0.83 | 1.15 |
| 11-07 03:32 | +10 stop | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 11-07 03:32 | +10 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 11-07 03:32 | +5 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 11-07 03:32 | +5 | HYPE | UP | 0.52 | no | -5.38 |
| 11-07 03:32 | +10 stop | HYPE | UP | 0.58 | 0.27 | -3.42 |
| 11-07 03:32 | +20 | HYPE | UP | 0.58 | no | -5.98 |
| 11-07 03:32 | +15 | HYPE | UP | 0.57 | no | -5.88 |
| 11-07 03:32 | +10 | HYPE | UP | 0.57 | no | -5.88 |
| 11-07 03:32 | +5 | HYPE | UP | 0.56 | 0.65 | 0.56 |
| 11-07 03:32 | +10 stop | NEAR | UP | 0.43 | 0.61 | 1.45 |
| 11-07 03:32 | +10 | NEAR | UP | 0.43 | 0.61 | 1.45 |
| 11-07 03:32 | +5 | NEAR | UP | 0.43 | 0.61 | 1.45 |
| 11-07 03:31 | +5 | ETH | UP | 0.57 | no | -5.88 |
| 11-07 03:31 | +10 stop | DOGE | UP | 0.61 | 0.41 | -2.34 |
| 11-07 03:31 | +20 | DOGE | UP | 0.61 | no | -6.27 |
| 11-07 03:31 | +15 | DOGE | UP | 0.62 | no | -6.37 |
| 11-07 03:31 | +10 | DOGE | UP | 0.62 | no | -6.37 |
| 11-07 03:31 | +5 | DOGE | UP | 0.62 | no | -6.37 |
| 11-07 03:31 | +10 stop | SOL | UP | 0.62 | 0.38 | -2.74 |
| 11-07 03:31 | +20 | SOL | UP | 0.62 | no | -6.37 |
| 11-07 03:31 | +15 | SOL | UP | 0.62 | no | -6.37 |
| 11-07 03:31 | +10 | SOL | UP | 0.62 | no | -6.37 |
| 11-07 03:31 | +5 | SOL | UP | 0.62 | no | -6.37 |
| 11-07 03:31 | +10 stop | BTC | UP | 0.65 | 0.48 | -2.04 |
| 11-07 03:31 | +20 | BTC | UP | 0.65 | no | -6.66 |
| 11-07 03:31 | +15 | BTC | UP | 0.65 | no | -6.66 |
| 11-07 03:31 | +10 | BTC | UP | 0.65 | no | -6.66 |
