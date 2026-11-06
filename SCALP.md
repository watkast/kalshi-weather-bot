# Range-Scalp Bot

*Updated Fri Nov 06 00:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48939 | 42638 | 6301 (75) | 1 | $-13943.86 | -4.5% |
| **+10¢** | 36536 | 29211 | 7325 (101) | 1 | $-12816.48 | -5.6% |
| **+15¢** | 30606 | 22718 | 7888 (130) | 1 | $-11697.17 | -6.1% |
| **+20¢** | 27198 | 18931 | 8267 (170) | 2 | $-10360.34 | -6.1% |
| **+10¢ (15¢ stop)** | 59670 | 59575 | 95 (57) | 0 | $-22106.80 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 00:48 | +5 | ZEC | UP | 0.62 | open |  |
| 11-06 00:47 | +10 stop | ZEC | UP | 0.62 | 0.42 | -2.35 |
| 11-06 00:47 | +10 | ZEC | UP | 0.63 | open |  |
| 11-06 00:47 | +5 | ZEC | UP | 0.63 | 0.69 | 0.28 |
| 11-06 00:47 | +10 stop | ZEC | DOWN | 0.43 | 0.54 | 0.74 |
| 11-06 00:47 | +20 | ZEC | DOWN | 0.43 | open |  |
| 11-06 00:47 | +15 | ZEC | DOWN | 0.43 | open |  |
| 11-06 00:47 | +10 | ZEC | DOWN | 0.43 | 0.54 | 0.74 |
| 11-06 00:47 | +5 | ZEC | DOWN | 0.43 | 0.54 | 0.74 |
| 11-06 00:47 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-06 00:47 | +20 | BNB | DOWN | 0.70 | 0.92 | 2.04 |
| 11-06 00:47 | +15 | BNB | DOWN | 0.70 | 0.86 | 1.36 |
| 11-06 00:47 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 11-06 00:47 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 11-06 00:46 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-06 00:46 | +20 | BTC | DOWN | 0.59 | 0.79 | 1.71 |
| 11-06 00:46 | +15 | BTC | DOWN | 0.59 | 0.75 | 1.29 |
| 11-06 00:46 | +10 | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 11-06 00:46 | +5 | BTC | DOWN | 0.60 | 0.69 | 0.58 |
| 11-06 00:46 | +10 stop | XRP | DOWN | 0.70 | 0.88 | 1.57 |
| 11-06 00:46 | +20 | XRP | DOWN | 0.70 | open |  |
| 11-06 00:46 | +15 | XRP | DOWN | 0.71 | 0.88 | 1.48 |
| 11-06 00:46 | +10 | XRP | DOWN | 0.71 | 0.88 | 1.47 |
| 11-06 00:46 | +10 stop | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-06 00:46 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-06 00:46 | +15 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-06 00:46 | +10 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-06 00:46 | +5 | DOGE | DOWN | 0.64 | 0.73 | 0.59 |
| 11-06 00:46 | +10 stop | SOL | DOWN | 0.65 | 0.84 | 1.64 |
| 11-06 00:46 | +20 | SOL | DOWN | 0.65 | 0.88 | 2.06 |
| 11-06 00:46 | +15 | SOL | DOWN | 0.65 | 0.84 | 1.64 |
| 11-06 00:46 | +10 | SOL | DOWN | 0.65 | 0.84 | 1.64 |
| 11-06 00:46 | +5 | SOL | DOWN | 0.65 | 0.70 | 0.19 |
| 11-06 00:46 | +10 stop | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-06 00:46 | +20 | ETH | DOWN | 0.65 | 0.88 | 2.07 |
| 11-06 00:46 | +15 | ETH | DOWN | 0.64 | 0.81 | 1.39 |
| 11-06 00:46 | +10 | ETH | DOWN | 0.64 | 0.79 | 1.21 |
| 11-06 00:46 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 11-06 00:46 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 11-06 00:33 | +10 stop | ETH | UP | 0.63 | 0.74 | 0.79 |
