# Range-Scalp Bot

*Updated Wed Nov 11 07:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55568 | 48459 | 7109 (94) | 1 | $-15197.97 | -4.3% |
| **+10¢** | 41518 | 33224 | 8294 (124) | 1 | $-14142.33 | -5.4% |
| **+15¢** | 34811 | 25867 | 8944 (158) | 1 | $-12905.38 | -5.9% |
| **+20¢** | 31003 | 21622 | 9381 (207) | 1 | $-11280.68 | -5.8% |
| **+10¢ (15¢ stop)** | 67681 | 67563 | 118 (73) | 1 | $-24919.37 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 07:00 | +10 stop | ETH | UP | 0.63 | open |  |
| 11-11 07:00 | +20 | ETH | UP | 0.63 | open |  |
| 11-11 07:00 | +15 | ETH | UP | 0.63 | open |  |
| 11-11 07:00 | +10 | ETH | UP | 0.63 | open |  |
| 11-11 07:00 | +5 | ETH | UP | 0.62 | open |  |
| 11-11 06:57 | +10 stop | ZEC | DOWN | 0.62 | 0.80 | 1.51 |
| 11-11 06:57 | +10 stop | DOGE | DOWN | 0.67 | 0.84 | 1.44 |
| 11-11 06:56 | +10 stop | ZEC | UP | 0.64 | 0.38 | -2.94 |
| 11-11 06:56 | +20 | ZEC | UP | 0.64 | no | -6.57 |
| 11-11 06:56 | +15 | ZEC | UP | 0.64 | no | -6.57 |
| 11-11 06:56 | +10 | ZEC | UP | 0.64 | no | -6.57 |
| 11-11 06:56 | +5 | ZEC | UP | 0.65 | no | -6.66 |
| 11-11 06:56 | +10 stop | DOGE | DOWN | 0.53 | 0.67 | 1.06 |
| 11-11 06:56 | +10 stop | HYPE | UP | 0.66 | 0.47 | -2.24 |
| 11-11 06:56 | +10 | HYPE | UP | 0.66 | 0.86 | 1.75 |
| 11-11 06:56 | +5 | HYPE | UP | 0.66 | 0.86 | 1.75 |
| 11-11 06:56 | +10 stop | BTC | UP | 0.48 | 0.14 | -3.67 |
| 11-11 06:56 | +10 stop | DOGE | UP | 0.41 | 0.59 | 1.46 |
| 11-11 06:55 | +10 stop | DOGE | DOWN | 0.51 | 0.69 | 1.47 |
| 11-11 06:55 | +10 stop | XRP | UP | 0.64 | 0.78 | 1.10 |
| 11-11 06:54 | +10 stop | HYPE | UP | 0.57 | 0.75 | 1.48 |
| 11-11 06:54 | +10 stop | BNB | DOWN | 0.65 | 0.48 | -2.04 |
| 11-11 06:53 | +10 stop | NEAR | UP | 0.68 | 0.82 | 1.08 |
| 11-11 06:52 | +10 stop | NEAR | UP | 0.59 | 0.74 | 1.19 |
| 11-11 06:51 | +5 | ZEC | UP | 0.68 | 0.74 | 0.30 |
| 11-11 06:51 | +10 stop | ZEC | UP | 0.69 | 0.83 | 1.15 |
| 11-11 06:51 | +10 | ZEC | UP | 0.69 | 0.83 | 1.15 |
| 11-11 06:51 | +10 stop | HYPE | UP | 0.67 | 0.44 | -2.64 |
| 11-11 06:51 | +5 | ZEC | UP | 0.63 | 0.69 | 0.28 |
| 11-11 06:50 | +5 | ZEC | UP | 0.54 | 0.59 | 0.15 |
| 11-11 06:50 | +10 stop | ZEC | UP | 0.54 | 0.66 | 0.86 |
| 11-11 06:49 | +5 | NEAR | DOWN | 0.70 | yes | -7.15 |
| 11-11 06:49 | +10 stop | HYPE | DOWN | 0.62 | 0.43 | -2.25 |
| 11-11 06:48 | +10 stop | XRP | DOWN | 0.61 | 0.46 | -1.85 |
| 11-11 06:48 | +10 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 11-11 06:48 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-11 06:48 | +10 stop | ZEC | DOWN | 0.66 | 0.49 | -2.04 |
| 11-11 06:48 | +10 stop | SOL | DOWN | 0.69 | 0.53 | -1.93 |
| 11-11 06:48 | +20 | SOL | DOWN | 0.69 | 0.91 | 1.98 |
| 11-11 06:48 | +10 stop | XRP | UP | 0.44 | 0.56 | 0.84 |
