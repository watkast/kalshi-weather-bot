# Range-Scalp Bot

*Updated Fri Nov 06 02:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49051 | 42739 | 6312 (75) | 0 | $-13938.70 | -4.5% |
| **+10¢** | 36621 | 29282 | 7339 (101) | 1 | $-12817.86 | -5.6% |
| **+15¢** | 30677 | 22775 | 7902 (130) | 1 | $-11688.79 | -6.1% |
| **+20¢** | 27263 | 18983 | 8280 (170) | 1 | $-10330.54 | -6.0% |
| **+10¢ (15¢ stop)** | 59827 | 59732 | 95 (57) | 1 | $-22178.80 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 02:30 | +10 stop | ETH | DOWN | 0.53 | open |  |
| 11-06 02:30 | +20 | ETH | DOWN | 0.53 | open |  |
| 11-06 02:30 | +15 | ETH | DOWN | 0.53 | open |  |
| 11-06 02:30 | +10 | ETH | DOWN | 0.53 | open |  |
| 11-06 02:30 | +5 | ETH | DOWN | 0.53 | 0.62 | 0.55 |
| 11-06 02:28 | +10 stop | DOGE | DOWN | 0.09 | 0.59 | 4.81 |
| 11-06 02:28 | +10 | DOGE | DOWN | 0.09 | 0.59 | 4.81 |
| 11-06 02:28 | +5 | DOGE | DOWN | 0.13 | 0.59 | 4.35 |
| 11-06 02:28 | +10 stop | HYPE | DOWN | 0.57 | 0.02 | -5.73 |
| 11-06 02:28 | +10 stop | HYPE | DOWN | 0.52 | 0.64 | 0.85 |
| 11-06 02:27 | +10 stop | ZEC | UP | 0.35 | 0.61 | 2.24 |
| 11-06 02:27 | +10 stop | BNB | UP | 0.29 | 0.55 | 2.27 |
| 11-06 02:26 | +10 stop | BTC | UP | 0.53 | 0.25 | -3.12 |
| 11-06 02:26 | +5 | BTC | UP | 0.53 | 0.87 | 3.14 |
| 11-06 02:26 | +10 stop | XRP | DOWN | 0.61 | 0.75 | 1.09 |
| 11-06 02:26 | +15 | XRP | DOWN | 0.62 | 0.86 | 2.14 |
| 11-06 02:26 | +10 | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 11-06 02:26 | +5 | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 11-06 02:26 | +5 | SOL | UP | 0.54 | 0.81 | 2.41 |
| 11-06 02:26 | +10 stop | DOGE | UP | 0.62 | 0.28 | -3.72 |
| 11-06 02:26 | +10 stop | SOL | UP | 0.56 | 0.29 | -3.03 |
| 11-06 02:26 | +5 | SOL | UP | 0.56 | 0.64 | 0.45 |
| 11-06 02:25 | +10 stop | NEAR | UP | 0.57 | 0.34 | -2.64 |
| 11-06 02:23 | +10 stop | NEAR | UP | 0.68 | 0.82 | 1.13 |
| 11-06 02:22 | +10 stop | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 11-06 02:22 | +10 stop | NEAR | UP | 0.49 | 0.61 | 0.85 |
| 11-06 02:21 | +10 stop | DOGE | UP | 0.62 | 0.73 | 0.79 |
| 11-06 02:21 | +10 stop | SOL | UP | 0.67 | 0.78 | 0.81 |
| 11-06 02:21 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 11-06 02:20 | +10 stop | XRP | DOWN | 0.43 | 0.58 | 1.14 |
| 11-06 02:20 | +20 | XRP | DOWN | 0.43 | 0.63 | 1.65 |
| 11-06 02:20 | +15 | XRP | DOWN | 0.43 | 0.58 | 1.14 |
| 11-06 02:20 | +10 | XRP | DOWN | 0.43 | 0.58 | 1.14 |
| 11-06 02:20 | +5 | XRP | DOWN | 0.43 | 0.58 | 1.14 |
| 11-06 02:19 | +10 stop | ETH | DOWN | 0.51 | 0.33 | -2.14 |
| 11-06 02:19 | +20 | ETH | DOWN | 0.53 | 0.89 | 3.35 |
| 11-06 02:19 | +15 | ETH | DOWN | 0.53 | 0.70 | 1.37 |
| 11-06 02:19 | +10 | ETH | DOWN | 0.53 | 0.70 | 1.37 |
| 11-06 02:19 | +5 | ETH | DOWN | 0.53 | 0.70 | 1.37 |
| 11-06 02:19 | +5 | BNB | DOWN | 0.54 | 0.70 | 1.29 |
