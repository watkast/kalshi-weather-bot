# Range-Scalp Bot

*Updated Sat Nov 07 04:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50426 | 43953 | 6473 (76) | 2 | $-14192.86 | -4.5% |
| **+10¢** | 37633 | 30097 | 7536 (102) | 2 | $-13122.71 | -5.5% |
| **+15¢** | 31513 | 23390 | 8123 (131) | 3 | $-12062.83 | -6.1% |
| **+20¢** | 28018 | 19503 | 8515 (173) | 3 | $-10659.16 | -6.1% |
| **+10¢ (15¢ stop)** | 61398 | 61299 | 99 (58) | 1 | $-22729.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 04:10 | +10 stop | BNB | UP | 0.60 | open |  |
| 11-07 04:10 | +5 | BNB | UP | 0.60 | open |  |
| 11-07 04:08 | +10 stop | BTC | DOWN | 0.62 | 0.79 | 1.41 |
| 11-07 04:07 | +10 stop | DOGE | DOWN | 0.70 | 0.85 | 1.29 |
| 11-07 04:07 | +10 | DOGE | DOWN | 0.70 | 0.85 | 1.29 |
| 11-07 04:07 | +5 | DOGE | DOWN | 0.70 | 0.79 | 0.66 |
| 11-07 04:07 | +10 stop | SOL | DOWN | 0.53 | 0.83 | 2.72 |
| 11-07 04:06 | +10 stop | ZEC | UP | 0.63 | 0.81 | 1.52 |
| 11-07 04:05 | +10 stop | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-07 04:05 | +10 | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-07 04:05 | +5 | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-07 04:05 | +10 stop | BNB | UP | 0.64 | 0.77 | 1.00 |
| 11-07 04:05 | +5 | BNB | UP | 0.64 | 0.77 | 1.00 |
| 11-07 04:04 | +10 stop | HYPE | UP | 0.68 | 0.81 | 1.03 |
| 11-07 04:04 | +10 stop | BTC | UP | 0.59 | 0.44 | -1.85 |
| 11-07 04:03 | +5 | HYPE | DOWN | 0.67 | open |  |
| 11-07 04:03 | +10 stop | SOL | DOWN | 0.67 | 0.50 | -2.04 |
| 11-07 04:03 | +10 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 11-07 04:03 | +5 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 11-07 04:03 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 11-07 04:03 | +10 stop | NEAR | DOWN | 0.63 | 0.85 | 1.94 |
| 11-07 04:03 | +5 | NEAR | DOWN | 0.63 | 0.72 | 0.58 |
| 11-07 04:03 | +5 | BNB | DOWN | 0.59 | 0.67 | 0.47 |
| 11-07 04:03 | +10 stop | BTC | DOWN | 0.59 | 0.39 | -2.34 |
| 11-07 04:03 | +10 stop | BNB | DOWN | 0.58 | 0.36 | -2.55 |
| 11-07 04:02 | +10 stop | BTC | DOWN | 0.53 | 0.66 | 0.96 |
| 11-07 04:02 | +10 stop | ZEC | UP | 0.71 | 0.55 | -1.91 |
| 11-07 04:02 | +20 | ZEC | UP | 0.70 | 0.93 | 2.14 |
| 11-07 04:02 | +15 | ZEC | UP | 0.70 | 0.86 | 1.36 |
| 11-07 04:02 | +10 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 11-07 04:02 | +5 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 11-07 04:01 | +10 stop | BNB | DOWN | 0.63 | 0.48 | -1.85 |
| 11-07 04:01 | +20 | BNB | DOWN | 0.63 | open |  |
| 11-07 04:01 | +15 | BNB | DOWN | 0.63 | open |  |
| 11-07 04:01 | +10 | BNB | DOWN | 0.63 | open |  |
| 11-07 04:01 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 11-07 04:01 | +10 stop | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-07 04:01 | +20 | ETH | DOWN | 0.71 | 0.95 | 2.22 |
| 11-07 04:01 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 11-07 04:01 | +10 | ETH | DOWN | 0.71 | 0.84 | 1.05 |
