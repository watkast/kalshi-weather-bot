# Range-Scalp Bot

*Updated Sat Oct 24 06:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31553 | 27504 | 4049 (40) | 1 | $-9064.17 | -4.6% |
| **+10¢** | 23594 | 18917 | 4677 (58) | 1 | $-8048.12 | -5.4% |
| **+15¢** | 19754 | 14726 | 5028 (81) | 3 | $-7187.91 | -5.8% |
| **+20¢** | 17502 | 12238 | 5264 (103) | 2 | $-6380.58 | -5.8% |
| **+10¢ (15¢ stop)** | 38725 | 38666 | 59 (32) | 0 | $-14779.02 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 06:04 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-24 06:04 | +15 | ZEC | DOWN | 0.70 | open |  |
| 10-24 06:04 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-24 06:04 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.42 |
| 10-24 06:04 | +10 stop | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-24 06:04 | +15 | BTC | DOWN | 0.70 | open |  |
| 10-24 06:04 | +10 | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-24 06:04 | +5 | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-24 06:01 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-24 06:01 | +20 | SOL | DOWN | 0.68 | open |  |
| 10-24 06:01 | +15 | SOL | DOWN | 0.68 | 0.83 | 1.24 |
| 10-24 06:01 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-24 06:01 | +5 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-24 06:01 | +10 stop | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-24 06:01 | +20 | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
| 10-24 06:01 | +15 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-24 06:01 | +10 | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-24 06:01 | +5 | ZEC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-24 06:01 | +10 stop | NEAR | DOWN | 0.69 | 0.80 | 0.79 |
| 10-24 06:01 | +20 | NEAR | DOWN | 0.69 | 0.92 | 2.09 |
| 10-24 06:01 | +15 | NEAR | DOWN | 0.69 | 0.85 | 1.32 |
| 10-24 06:01 | +10 | NEAR | DOWN | 0.69 | 0.80 | 0.79 |
| 10-24 06:01 | +5 | NEAR | DOWN | 0.69 | 0.80 | 0.79 |
| 10-24 06:01 | +10 stop | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 10-24 06:01 | +20 | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 10-24 06:01 | +15 | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 10-24 06:01 | +10 | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 10-24 06:01 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.39 |
| 10-24 06:01 | +10 stop | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-24 06:01 | +20 | HYPE | DOWN | 0.60 | 0.80 | 1.71 |
| 10-24 06:01 | +15 | HYPE | DOWN | 0.60 | 0.80 | 1.71 |
| 10-24 06:01 | +10 | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-24 06:01 | +5 | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-24 06:01 | +10 stop | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 10-24 06:01 | +20 | XRP | DOWN | 0.64 | 0.87 | 2.05 |
| 10-24 06:01 | +15 | XRP | DOWN | 0.64 | 0.81 | 1.42 |
| 10-24 06:01 | +10 | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 10-24 06:01 | +5 | XRP | DOWN | 0.64 | 0.77 | 1.00 |
| 10-24 06:01 | +10 stop | ETH | UP | 0.54 | 0.38 | -1.95 |
| 10-24 06:01 | +20 | ETH | UP | 0.54 | open |  |
