# Range-Scalp Bot

*Updated Fri Oct 09 16:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9132 | 7886 | 1246 (16) | 0 | $-3062.10 | -5.3% |
| **+10¢** | 6912 | 5452 | 1460 (28) | 0 | $-2946.12 | -6.8% |
| **+15¢** | 5831 | 4293 | 1538 (41) | 0 | $-2409.94 | -6.6% |
| **+20¢** | 5191 | 3592 | 1599 (52) | 0 | $-2002.32 | -6.1% |
| **+10¢ (15¢ stop)** | 11173 | 11141 | 32 (20) | 0 | $-4276.46 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 16:12 | +10 stop | BTC | DOWN | 0.47 | 0.12 | -3.76 |
| 10-09 16:12 | +20 | BTC | DOWN | 0.47 | yes | -4.88 |
| 10-09 16:12 | +15 | BTC | DOWN | 0.47 | yes | -4.88 |
| 10-09 16:12 | +10 | BTC | DOWN | 0.48 | yes | -4.98 |
| 10-09 16:12 | +5 | BTC | DOWN | 0.54 | yes | -5.58 |
| 10-09 16:11 | +10 stop | ZEC | DOWN | 0.55 | 0.25 | -3.32 |
| 10-09 16:11 | +15 | ZEC | DOWN | 0.55 | yes | -5.68 |
| 10-09 16:11 | +10 | ZEC | DOWN | 0.55 | yes | -5.68 |
| 10-09 16:11 | +5 | ZEC | DOWN | 0.55 | 0.63 | 0.45 |
| 10-09 16:10 | +5 | HYPE | DOWN | 0.66 | yes | -6.76 |
| 10-09 16:10 | +10 stop | HYPE | DOWN | 0.65 | 0.29 | -3.95 |
| 10-09 16:09 | +10 stop | SOL | UP | 0.68 | 0.43 | -2.84 |
| 10-09 16:09 | +15 | SOL | UP | 0.68 | 0.84 | 1.34 |
| 10-09 16:09 | +10 | SOL | UP | 0.68 | 0.84 | 1.34 |
| 10-09 16:09 | +5 | SOL | UP | 0.69 | 0.74 | 0.21 |
| 10-09 16:09 | +10 stop | ZEC | DOWN | 0.60 | 0.71 | 0.73 |
| 10-09 16:09 | +5 | BTC | UP | 0.39 | 0.55 | 1.25 |
| 10-09 16:08 | +10 stop | BTC | DOWN | 0.53 | 0.72 | 1.57 |
| 10-09 16:08 | +10 stop | HYPE | UP | 0.65 | 0.47 | -2.14 |
| 10-09 16:08 | +10 stop | BTC | UP | 0.40 | 0.54 | 1.05 |
| 10-09 16:07 | +10 stop | ZEC | UP | 0.65 | 0.46 | -2.24 |
| 10-09 16:06 | +10 stop | BTC | DOWN | 0.53 | 0.37 | -1.95 |
| 10-09 16:06 | +20 | BTC | DOWN | 0.53 | 0.73 | 1.68 |
| 10-09 16:06 | +15 | BTC | DOWN | 0.53 | 0.72 | 1.57 |
| 10-09 16:06 | +10 | BTC | DOWN | 0.53 | 0.72 | 1.57 |
| 10-09 16:06 | +5 | BTC | DOWN | 0.53 | 0.58 | 0.14 |
| 10-09 16:06 | +10 stop | SOL | UP | 0.64 | 0.80 | 1.31 |
| 10-09 16:06 | +20 | SOL | UP | 0.64 | 0.84 | 1.73 |
| 10-09 16:06 | +15 | SOL | UP | 0.64 | 0.80 | 1.31 |
| 10-09 16:06 | +10 | SOL | UP | 0.64 | 0.80 | 1.31 |
| 10-09 16:06 | +5 | SOL | UP | 0.64 | 0.80 | 1.31 |
| 10-09 16:05 | +10 stop | BNB | UP | 0.57 | 0.69 | 0.88 |
| 10-09 16:05 | +5 | BNB | UP | 0.57 | 0.69 | 0.89 |
| 10-09 16:05 | +10 stop | HYPE | UP | 0.60 | 0.70 | 0.68 |
| 10-09 16:05 | +5 | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-09 16:05 | +10 stop | XRP | UP | 0.63 | 0.77 | 1.10 |
| 10-09 16:05 | +20 | XRP | UP | 0.63 | 0.83 | 1.73 |
| 10-09 16:05 | +15 | XRP | UP | 0.63 | 0.78 | 1.20 |
| 10-09 16:05 | +10 | XRP | UP | 0.63 | 0.77 | 1.11 |
| 10-09 16:05 | +5 | XRP | UP | 0.63 | 0.68 | 0.18 |
