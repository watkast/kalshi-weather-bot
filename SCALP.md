# Range-Scalp Bot

*Updated Wed Oct 07 01:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5760 | 4987 | 773 (9) | 1 | $-1807.17 | -5.0% |
| **+10¢** | 4390 | 3481 | 909 (16) | 2 | $-1716.41 | -6.2% |
| **+15¢** | 3683 | 2719 | 964 (20) | 2 | $-1509.17 | -6.5% |
| **+20¢** | 3289 | 2285 | 1004 (27) | 3 | $-1251.47 | -6.1% |
| **+10¢ (15¢ stop)** | 7010 | 6995 | 15 (9) | 0 | $-2507.07 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 01:20 | +10 stop | NEAR | DOWN | 0.64 | 0.83 | 1.63 |
| 10-07 01:20 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 10-07 01:19 | +10 stop | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 10-07 01:19 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 10-07 01:18 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.28 |
| 10-07 01:18 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-07 01:18 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-07 01:18 | +5 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-07 01:18 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.49 |
| 10-07 01:17 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 10-07 01:17 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.77 |
| 10-07 01:17 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.31 |
| 10-07 01:17 | +10 stop | HYPE | UP | 0.53 | 0.37 | -1.95 |
| 10-07 01:17 | +10 | HYPE | UP | 0.55 | open |  |
| 10-07 01:17 | +5 | HYPE | UP | 0.55 | open |  |
| 10-07 01:17 | +10 stop | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 10-07 01:17 | +15 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 10-07 01:17 | +10 | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 10-07 01:17 | +5 | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 10-07 01:16 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-07 01:16 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.87 |
| 10-07 01:16 | +15 | XRP | DOWN | 0.70 | 0.88 | 1.57 |
| 10-07 01:16 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-07 01:16 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 10-07 01:16 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-07 01:16 | +20 | DOGE | DOWN | 0.71 | 0.93 | 2.00 |
| 10-07 01:16 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 10-07 01:16 | +10 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-07 01:16 | +5 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-07 01:16 | +10 stop | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-07 01:16 | +20 | BTC | DOWN | 0.62 | 0.85 | 2.04 |
| 10-07 01:16 | +15 | BTC | DOWN | 0.62 | 0.80 | 1.51 |
| 10-07 01:16 | +10 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-07 01:16 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-07 01:16 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-07 01:16 | +20 | SOL | DOWN | 0.64 | 0.85 | 1.84 |
| 10-07 01:16 | +15 | SOL | DOWN | 0.64 | 0.79 | 1.21 |
| 10-07 01:16 | +10 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-07 01:16 | +5 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-07 01:16 | +10 stop | ZEC | DOWN | 0.68 | 0.81 | 1.02 |
