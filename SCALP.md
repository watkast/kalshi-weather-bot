# Range-Scalp Bot

*Updated Sat Oct 24 10:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31895 | 27806 | 4089 (40) | 2 | $-9139.07 | -4.5% |
| **+10¢** | 23857 | 19129 | 4728 (58) | 3 | $-8146.04 | -5.4% |
| **+15¢** | 19971 | 14888 | 5083 (81) | 3 | $-7286.65 | -5.8% |
| **+20¢** | 17692 | 12371 | 5321 (103) | 3 | $-6466.13 | -5.8% |
| **+10¢ (15¢ stop)** | 39183 | 39124 | 59 (32) | 0 | $-14964.91 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 10:56 | +10 stop | DOGE | DOWN | 0.58 | 0.29 | -3.20 |
| 10-24 10:56 | +20 | DOGE | DOWN | 0.58 | open |  |
| 10-24 10:56 | +15 | DOGE | DOWN | 0.58 | open |  |
| 10-24 10:56 | +10 | DOGE | DOWN | 0.58 | open |  |
| 10-24 10:56 | +5 | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-24 10:52 | +10 stop | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-24 10:52 | +20 | DOGE | DOWN | 0.65 | 0.87 | 1.96 |
| 10-24 10:52 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-24 10:52 | +10 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-24 10:52 | +5 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-24 10:51 | +10 stop | SOL | DOWN | 0.63 | 0.79 | 1.28 |
| 10-24 10:51 | +10 stop | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 10-24 10:51 | +20 | BTC | DOWN | 0.59 | 0.85 | 2.34 |
| 10-24 10:51 | +15 | BTC | DOWN | 0.59 | 0.76 | 1.40 |
| 10-24 10:51 | +10 | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-24 10:51 | +5 | BTC | DOWN | 0.60 | 0.69 | 0.58 |
| 10-24 10:50 | +5 | HYPE | DOWN | 0.67 | 0.74 | 0.40 |
| 10-24 10:49 | +10 stop | SOL | UP | 0.53 | 0.36 | -2.05 |
| 10-24 10:47 | +10 stop | HYPE | DOWN | 0.58 | 0.74 | 1.24 |
| 10-24 10:47 | +20 | HYPE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-24 10:47 | +15 | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-24 10:47 | +10 | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 10-24 10:47 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.27 |
| 10-24 10:46 | +10 stop | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 10-24 10:46 | +20 | ETH | DOWN | 0.57 | 0.78 | 1.79 |
| 10-24 10:46 | +15 | ETH | DOWN | 0.57 | 0.72 | 1.17 |
| 10-24 10:46 | +10 | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 10-24 10:46 | +5 | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 10-24 10:46 | +10 stop | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 10:46 | +20 | BNB | DOWN | 0.64 | 0.84 | 1.73 |
| 10-24 10:46 | +15 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-24 10:46 | +10 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 10:46 | +5 | BNB | DOWN | 0.64 | 0.70 | 0.28 |
| 10-24 10:46 | +10 stop | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 10:46 | +20 | ZEC | DOWN | 0.64 | 0.92 | 2.59 |
| 10-24 10:46 | +15 | ZEC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-24 10:46 | +10 | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 10:46 | +5 | ZEC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-24 10:46 | +10 stop | XRP | UP | 0.55 | 0.35 | -2.34 |
| 10-24 10:46 | +20 | XRP | UP | 0.55 | open |  |
