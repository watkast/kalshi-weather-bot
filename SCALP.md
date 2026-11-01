# Range-Scalp Bot

*Updated Sun Nov 01 02:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43042 | 37523 | 5519 (62) | 1 | $-12192.45 | -4.5% |
| **+10¢** | 32099 | 25720 | 6379 (84) | 1 | $-10931.98 | -5.4% |
| **+15¢** | 26849 | 19971 | 6878 (112) | 1 | $-10028.69 | -5.9% |
| **+20¢** | 23847 | 16643 | 7204 (145) | 4 | $-8850.78 | -5.9% |
| **+10¢ (15¢ stop)** | 52492 | 52409 | 83 (48) | 1 | $-19873.48 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 02:02 | +5 | ETH | UP | 0.68 | open |  |
| 11-01 02:01 | +10 stop | HYPE | UP | 0.67 | 0.79 | 0.88 |
| 11-01 02:01 | +20 | HYPE | UP | 0.67 | open |  |
| 11-01 02:01 | +15 | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 11-01 02:01 | +10 | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 11-01 02:01 | +5 | HYPE | UP | 0.67 | 0.72 | 0.19 |
| 11-01 02:00 | +10 stop | BNB | UP | 0.57 | 0.71 | 1.07 |
| 11-01 02:00 | +20 | BNB | UP | 0.57 | open |  |
| 11-01 02:00 | +15 | BNB | UP | 0.57 | 0.74 | 1.38 |
| 11-01 02:00 | +10 | BNB | UP | 0.57 | 0.71 | 1.07 |
| 11-01 02:00 | +5 | BNB | UP | 0.57 | 0.71 | 1.07 |
| 11-01 02:00 | +10 stop | ETH | UP | 0.57 | open |  |
| 11-01 02:00 | +20 | ETH | UP | 0.57 | open |  |
| 11-01 02:00 | +15 | ETH | UP | 0.57 | open |  |
| 11-01 02:00 | +10 | ETH | UP | 0.57 | open |  |
| 11-01 02:00 | +5 | ETH | UP | 0.57 | 0.63 | 0.25 |
| 11-01 02:00 | +10 stop | ZEC | UP | 0.62 | 0.75 | 0.99 |
| 11-01 02:00 | +20 | ZEC | UP | 0.62 | open |  |
| 11-01 02:00 | +15 | ZEC | UP | 0.62 | 0.79 | 1.41 |
| 11-01 02:00 | +10 | ZEC | UP | 0.62 | 0.75 | 0.99 |
| 11-01 02:00 | +5 | ZEC | UP | 0.62 | 0.75 | 0.99 |
| 11-01 01:49 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-01 01:49 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-01 01:49 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 11-01 01:47 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.80 |
| 11-01 01:47 | +20 | HYPE | DOWN | 0.70 | 0.93 | 2.07 |
| 11-01 01:47 | +15 | HYPE | DOWN | 0.70 | 0.86 | 1.31 |
| 11-01 01:47 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.79 |
| 11-01 01:47 | +5 | HYPE | DOWN | 0.70 | 0.81 | 0.79 |
| 11-01 01:47 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 11-01 01:46 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-01 01:46 | +20 | NEAR | DOWN | 0.61 | 0.83 | 1.93 |
| 11-01 01:46 | +15 | NEAR | DOWN | 0.61 | 0.77 | 1.30 |
| 11-01 01:46 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-01 01:46 | +5 | NEAR | DOWN | 0.61 | 0.66 | 0.17 |
| 11-01 01:41 | +10 stop | BNB | DOWN | 0.54 | 0.65 | 0.72 |
| 11-01 01:40 | +10 stop | BNB | UP | 0.63 | 0.35 | -3.13 |
| 11-01 01:40 | +20 | BNB | UP | 0.63 | 0.90 | 2.46 |
| 11-01 01:40 | +15 | BNB | UP | 0.63 | 0.79 | 1.31 |
| 11-01 01:40 | +10 | BNB | UP | 0.63 | 0.79 | 1.31 |
