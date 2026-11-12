# Range-Scalp Bot

*Updated Thu Nov 12 11:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56830 | 49537 | 7293 (101) | 0 | $-15664.42 | -4.4% |
| **+10¢** | 42476 | 33969 | 8507 (133) | 0 | $-14583.70 | -5.5% |
| **+15¢** | 35614 | 26457 | 9157 (167) | 0 | $-13208.60 | -5.9% |
| **+20¢** | 31723 | 22115 | 9608 (217) | 1 | $-11599.41 | -5.8% |
| **+10¢ (15¢ stop)** | 69298 | 69170 | 128 (78) | 0 | $-25603.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 11:31 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-12 11:31 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-12 11:31 | +15 | NEAR | DOWN | 0.68 | 0.84 | 1.34 |
| 11-12 11:31 | +10 | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-12 11:31 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 11-12 11:31 | +10 stop | ZEC | DOWN | 0.63 | 0.86 | 2.04 |
| 11-12 11:31 | +20 | ZEC | DOWN | 0.64 | 0.86 | 1.94 |
| 11-12 11:31 | +15 | ZEC | DOWN | 0.66 | 0.86 | 1.75 |
| 11-12 11:31 | +10 | ZEC | DOWN | 0.66 | 0.86 | 1.75 |
| 11-12 11:31 | +5 | ZEC | DOWN | 0.66 | 0.86 | 1.75 |
| 11-12 11:25 | +10 stop | ZEC | UP | 0.63 | 0.48 | -1.85 |
| 11-12 11:23 | +10 stop | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 11-12 11:23 | +15 | ETH | DOWN | 0.61 | 0.79 | 1.51 |
| 11-12 11:23 | +10 | ETH | DOWN | 0.61 | 0.79 | 1.51 |
| 11-12 11:23 | +5 | ETH | DOWN | 0.61 | 0.70 | 0.58 |
| 11-12 11:22 | +10 stop | HYPE | DOWN | 0.55 | 0.80 | 2.19 |
| 11-12 11:22 | +20 | HYPE | DOWN | 0.55 | 0.80 | 2.19 |
| 11-12 11:22 | +15 | HYPE | DOWN | 0.55 | 0.80 | 2.19 |
| 11-12 11:22 | +10 | HYPE | DOWN | 0.56 | 0.80 | 2.10 |
| 11-12 11:22 | +5 | HYPE | DOWN | 0.56 | 0.80 | 2.10 |
| 11-12 11:22 | +10 stop | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 11-12 11:22 | +20 | NEAR | DOWN | 0.59 | 0.85 | 2.34 |
| 11-12 11:22 | +15 | NEAR | DOWN | 0.59 | 0.85 | 2.34 |
| 11-12 11:22 | +10 | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 11-12 11:22 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 11-12 11:20 | +10 stop | ZEC | UP | 0.58 | 0.76 | 1.49 |
| 11-12 11:19 | +10 stop | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-12 11:19 | +20 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 11-12 11:19 | +15 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 11-12 11:19 | +10 | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-12 11:19 | +5 | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-12 11:18 | +10 stop | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 11-12 11:18 | +10 | ETH | DOWN | 0.69 | 0.84 | 1.25 |
| 11-12 11:18 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 11-12 11:17 | +10 stop | ZEC | DOWN | 0.71 | 0.50 | -2.43 |
| 11-12 11:17 | +20 | ZEC | DOWN | 0.71 | 0.93 | 1.95 |
| 11-12 11:17 | +15 | ZEC | DOWN | 0.71 | 0.93 | 1.95 |
| 11-12 11:17 | +10 | ZEC | DOWN | 0.71 | 0.93 | 1.95 |
| 11-12 11:17 | +5 | ZEC | DOWN | 0.71 | 0.93 | 1.95 |
| 11-12 11:16 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
