# Range-Scalp Bot

*Updated Sun Oct 25 02:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32399 | 28251 | 4148 (41) | 1 | $-9229.21 | -4.5% |
| **+10¢** | 24253 | 19448 | 4805 (59) | 1 | $-8273.86 | -5.4% |
| **+15¢** | 20311 | 15144 | 5167 (82) | 1 | $-7395.80 | -5.8% |
| **+20¢** | 17992 | 12586 | 5406 (104) | 1 | $-6533.82 | -5.8% |
| **+10¢ (15¢ stop)** | 39806 | 39746 | 60 (32) | 0 | $-15201.37 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 02:09 | +10 stop | NEAR | DOWN | 0.67 | 0.46 | -2.44 |
| 10-25 02:09 | +15 | NEAR | DOWN | 0.67 | 0.91 | 2.16 |
| 10-25 02:09 | +10 | NEAR | DOWN | 0.67 | 0.91 | 2.16 |
| 10-25 02:09 | +5 | NEAR | DOWN | 0.63 | 0.75 | 0.91 |
| 10-25 02:09 | +10 stop | SOL | UP | 0.68 | 0.83 | 1.24 |
| 10-25 02:09 | +20 | SOL | UP | 0.68 | 0.89 | 1.87 |
| 10-25 02:09 | +15 | SOL | UP | 0.68 | 0.83 | 1.24 |
| 10-25 02:09 | +10 | SOL | UP | 0.68 | 0.83 | 1.24 |
| 10-25 02:09 | +5 | SOL | UP | 0.68 | 0.76 | 0.51 |
| 10-25 02:09 | +10 stop | DOGE | UP | 0.64 | 0.77 | 1.00 |
| 10-25 02:09 | +20 | DOGE | UP | 0.64 | 0.84 | 1.73 |
| 10-25 02:09 | +15 | DOGE | UP | 0.62 | 0.77 | 1.20 |
| 10-25 02:09 | +10 | DOGE | UP | 0.62 | 0.77 | 1.20 |
| 10-25 02:09 | +5 | DOGE | UP | 0.63 | 0.77 | 1.10 |
| 10-25 02:06 | +5 | NEAR | UP | 0.64 | 0.69 | 0.18 |
| 10-25 02:06 | +10 stop | ETH | UP | 0.70 | 0.81 | 0.84 |
| 10-25 02:06 | +10 | ETH | UP | 0.70 | 0.81 | 0.84 |
| 10-25 02:06 | +5 | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-25 02:05 | +10 stop | NEAR | UP | 0.67 | 0.79 | 0.92 |
| 10-25 02:05 | +10 stop | HYPE | UP | 0.70 | 0.85 | 1.26 |
| 10-25 02:05 | +15 | HYPE | UP | 0.70 | 0.85 | 1.26 |
| 10-25 02:05 | +10 stop | ZEC | UP | 0.66 | 0.79 | 1.02 |
| 10-25 02:04 | +10 stop | ETH | DOWN | 0.51 | 0.35 | -1.94 |
| 10-25 02:04 | +10 stop | BNB | DOWN | 0.57 | 0.31 | -2.93 |
| 10-25 02:04 | +15 | BNB | DOWN | 0.57 | open |  |
| 10-25 02:04 | +10 | BNB | DOWN | 0.57 | open |  |
| 10-25 02:04 | +5 | BNB | DOWN | 0.57 | open |  |
| 10-25 02:04 | +5 | ETH | DOWN | 0.63 | 0.70 | 0.38 |
| 10-25 02:04 | +10 stop | HYPE | UP | 0.46 | 0.62 | 1.25 |
| 10-25 02:04 | +20 | HYPE | UP | 0.46 | 0.70 | 2.07 |
| 10-25 02:04 | +15 | HYPE | UP | 0.46 | 0.62 | 1.25 |
| 10-25 02:03 | +10 stop | NEAR | DOWN | 0.67 | 0.50 | -2.04 |
| 10-25 02:03 | +5 | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 10-25 02:03 | +5 | XRP | UP | 0.62 | 0.74 | 0.89 |
| 10-25 02:03 | +5 | SOL | UP | 0.67 | 0.72 | 0.19 |
| 10-25 02:02 | +5 | ETH | DOWN | 0.57 | 0.62 | 0.15 |
| 10-25 02:02 | +10 stop | XRP | UP | 0.71 | 0.83 | 0.95 |
| 10-25 02:02 | +20 | XRP | UP | 0.71 | 0.91 | 1.83 |
| 10-25 02:02 | +15 | XRP | UP | 0.71 | 0.87 | 1.37 |
| 10-25 02:02 | +10 | XRP | UP | 0.71 | 0.83 | 0.95 |
