# Range-Scalp Bot

*Updated Fri Oct 23 22:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31067 | 27071 | 3996 (40) | 0 | $-8990.40 | -4.6% |
| **+10¢** | 23235 | 18619 | 4616 (58) | 0 | $-7994.65 | -5.5% |
| **+15¢** | 19439 | 14473 | 4966 (81) | 0 | $-7200.06 | -5.9% |
| **+20¢** | 17217 | 12016 | 5201 (103) | 0 | $-6453.65 | -6.0% |
| **+10¢ (15¢ stop)** | 38120 | 38061 | 59 (32) | 0 | $-14609.58 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 22:29 | +10 stop | BNB | DOWN | 0.60 | 0.37 | -2.64 |
| 10-23 22:29 | +5 | BNB | DOWN | 0.60 | yes | -6.22 |
| 10-23 22:27 | +5 | BNB | UP | 0.63 | 0.76 | 1.00 |
| 10-23 22:27 | +10 stop | BTC | UP | 0.65 | 0.50 | -1.84 |
| 10-23 22:26 | +10 stop | BNB | UP | 0.55 | 0.76 | 1.79 |
| 10-23 22:26 | +5 | BNB | UP | 0.56 | 0.62 | 0.25 |
| 10-23 22:24 | +10 stop | BNB | DOWN | 0.60 | 0.33 | -3.03 |
| 10-23 22:24 | +10 stop | BTC | DOWN | 0.59 | 0.32 | -3.03 |
| 10-23 22:24 | +15 | BTC | DOWN | 0.59 | no | 3.93 |
| 10-23 22:24 | +10 | BTC | DOWN | 0.59 | no | 3.93 |
| 10-23 22:24 | +5 | BTC | DOWN | 0.59 | no | 3.93 |
| 10-23 22:23 | +10 stop | HYPE | UP | 0.56 | 0.40 | -1.95 |
| 10-23 22:23 | +5 | ETH | DOWN | 0.65 | 0.86 | 1.85 |
| 10-23 22:22 | +10 stop | BNB | UP | 0.56 | 0.41 | -1.85 |
| 10-23 22:22 | +10 stop | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 10-23 22:22 | +10 | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 10-23 22:22 | +5 | ETH | DOWN | 0.58 | 0.63 | 0.15 |
| 10-23 22:22 | +5 | SOL | DOWN | 0.58 | 0.65 | 0.36 |
| 10-23 22:22 | +10 stop | HYPE | DOWN | 0.71 | 0.46 | -2.83 |
| 10-23 22:21 | +10 stop | SOL | DOWN | 0.58 | 0.71 | 0.97 |
| 10-23 22:21 | +20 | SOL | DOWN | 0.58 | 0.89 | 2.85 |
| 10-23 22:21 | +15 | SOL | DOWN | 0.58 | 0.73 | 1.18 |
| 10-23 22:21 | +10 | SOL | DOWN | 0.58 | 0.71 | 0.97 |
| 10-23 22:21 | +5 | SOL | DOWN | 0.58 | 0.66 | 0.46 |
| 10-23 22:21 | +10 stop | BNB | DOWN | 0.62 | 0.45 | -2.05 |
| 10-23 22:21 | +20 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-23 22:21 | +15 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-23 22:21 | +10 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-23 22:21 | +5 | BNB | DOWN | 0.62 | 0.68 | 0.27 |
| 10-23 22:21 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 10-23 22:21 | +15 | ETH | DOWN | 0.64 | 0.86 | 1.94 |
| 10-23 22:21 | +10 | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 10-23 22:21 | +5 | ETH | DOWN | 0.64 | 0.71 | 0.38 |
| 10-23 22:17 | +5 | DOGE | UP | 0.64 | 0.71 | 0.38 |
| 10-23 22:17 | +5 | XRP | UP | 0.69 | 0.74 | 0.21 |
| 10-23 22:16 | +10 stop | HYPE | UP | 0.70 | 0.29 | -4.40 |
| 10-23 22:16 | +20 | HYPE | UP | 0.70 | no | -7.15 |
| 10-23 22:16 | +15 | HYPE | UP | 0.70 | no | -7.15 |
| 10-23 22:16 | +10 | HYPE | UP | 0.70 | no | -7.15 |
| 10-23 22:16 | +5 | HYPE | UP | 0.70 | no | -7.15 |
