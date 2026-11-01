# Range-Scalp Bot

*Updated Sun Nov 01 00:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42915 | 37416 | 5499 (62) | 4 | $-12130.70 | -4.5% |
| **+10¢** | 32002 | 25643 | 6359 (84) | 4 | $-10888.96 | -5.4% |
| **+15¢** | 26774 | 19918 | 6856 (112) | 4 | $-9971.85 | -5.9% |
| **+20¢** | 23782 | 16596 | 7186 (145) | 4 | $-8835.17 | -5.9% |
| **+10¢ (15¢ stop)** | 52344 | 52261 | 83 (48) | 4 | $-19836.39 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 00:02 | +10 stop | HYPE | UP | 0.57 | open |  |
| 11-01 00:02 | +20 | HYPE | UP | 0.57 | open |  |
| 11-01 00:02 | +15 | HYPE | UP | 0.57 | open |  |
| 11-01 00:02 | +10 | HYPE | UP | 0.57 | open |  |
| 11-01 00:02 | +5 | HYPE | UP | 0.57 | open |  |
| 11-01 00:02 | +10 stop | ZEC | DOWN | 0.69 | open |  |
| 11-01 00:02 | +20 | ZEC | DOWN | 0.69 | open |  |
| 11-01 00:02 | +15 | ZEC | DOWN | 0.69 | open |  |
| 11-01 00:02 | +10 | ZEC | DOWN | 0.69 | open |  |
| 11-01 00:02 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-01 00:02 | +10 stop | BNB | DOWN | 0.56 | open |  |
| 11-01 00:02 | +20 | BNB | DOWN | 0.56 | open |  |
| 11-01 00:02 | +15 | BNB | DOWN | 0.56 | open |  |
| 11-01 00:02 | +10 | BNB | DOWN | 0.56 | open |  |
| 11-01 00:02 | +5 | BNB | DOWN | 0.56 | open |  |
| 11-01 00:01 | +10 stop | NEAR | DOWN | 0.65 | open |  |
| 11-01 00:01 | +20 | NEAR | DOWN | 0.65 | open |  |
| 11-01 00:01 | +15 | NEAR | DOWN | 0.65 | open |  |
| 11-01 00:01 | +10 | NEAR | DOWN | 0.65 | open |  |
| 11-01 00:01 | +5 | NEAR | DOWN | 0.65 | open |  |
| 10-31 23:58 | +10 stop | XRP | UP | 0.54 | 0.82 | 2.51 |
| 10-31 23:57 | +10 stop | DOGE | DOWN | 0.51 | 0.20 | -3.40 |
| 10-31 23:55 | +10 stop | HYPE | UP | 0.64 | 0.43 | -2.45 |
| 10-31 23:53 | +10 stop | XRP | DOWN | 0.55 | 0.37 | -2.15 |
| 10-31 23:53 | +10 stop | DOGE | UP | 0.58 | 0.41 | -2.05 |
| 10-31 23:52 | +10 stop | XRP | DOWN | 0.49 | 0.59 | 0.65 |
| 10-31 23:51 | +5 | XRP | UP | 0.65 | 0.82 | 1.43 |
| 10-31 23:49 | +10 stop | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-31 23:48 | +10 stop | SOL | UP | 0.58 | 0.72 | 1.07 |
| 10-31 23:48 | +20 | SOL | UP | 0.58 | 0.81 | 2.01 |
| 10-31 23:48 | +15 | SOL | UP | 0.58 | 0.73 | 1.18 |
| 10-31 23:48 | +10 | SOL | UP | 0.58 | 0.72 | 1.07 |
| 10-31 23:48 | +5 | SOL | UP | 0.57 | 0.72 | 1.17 |
| 10-31 23:48 | +5 | ETH | UP | 0.67 | 0.75 | 0.50 |
| 10-31 23:48 | +20 | BNB | UP | 0.71 | 0.91 | 1.82 |
| 10-31 23:48 | +15 | BNB | UP | 0.71 | 0.90 | 1.68 |
| 10-31 23:48 | +10 | BNB | UP | 0.71 | 0.83 | 0.95 |
| 10-31 23:48 | +5 | BNB | UP | 0.71 | 0.78 | 0.42 |
| 10-31 23:47 | +10 stop | ZEC | DOWN | 0.59 | 0.43 | -1.95 |
| 10-31 23:47 | +10 stop | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
