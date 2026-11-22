# Range-Scalp Bot

*Updated Sun Nov 22 02:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68126 | 59454 | 8672 (138) | 0 | $-18288.59 | -4.3% |
| **+10¢** | 50862 | 40733 | 10129 (181) | 0 | $-16957.32 | -5.3% |
| **+15¢** | 42638 | 31718 | 10920 (231) | 0 | $-15210.69 | -5.7% |
| **+20¢** | 37957 | 26480 | 11477 (289) | 0 | $-13541.18 | -5.7% |
| **+10¢ (15¢ stop)** | 82938 | 82759 | 179 (111) | 0 | $-30431.83 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 02:13 | +10 stop | ETH | DOWN | 0.70 | no | 2.85 |
| 11-22 02:12 | +10 stop | ETH | DOWN | 0.71 | 0.56 | -1.83 |
| 11-22 02:11 | +10 stop | ETH | DOWN | 0.51 | 0.63 | 0.85 |
| 11-22 02:10 | +10 stop | SOL | UP | 0.70 | 0.81 | 0.85 |
| 11-22 02:10 | +20 | SOL | UP | 0.71 | yes | 2.76 |
| 11-22 02:10 | +15 | SOL | UP | 0.71 | yes | 2.76 |
| 11-22 02:10 | +5 | SOL | UP | 0.71 | 0.79 | 0.54 |
| 11-22 02:10 | +10 stop | ETH | UP | 0.61 | 0.40 | -2.44 |
| 11-22 02:10 | +10 | ETH | UP | 0.62 | no | -6.37 |
| 11-22 02:10 | +5 | ETH | UP | 0.62 | no | -6.37 |
| 11-22 02:09 | +10 stop | BNB | DOWN | 0.70 | 0.41 | -3.22 |
| 11-22 02:09 | +10 stop | ETH | UP | 0.60 | 0.76 | 1.30 |
| 11-22 02:09 | +5 | ETH | UP | 0.60 | 0.76 | 1.30 |
| 11-22 02:09 | +10 stop | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 11-22 02:09 | +10 stop | HYPE | UP | 0.71 | 0.87 | 1.37 |
| 11-22 02:08 | +10 stop | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-22 02:08 | +5 | BTC | DOWN | 0.57 | 0.69 | 0.87 |
| 11-22 02:08 | +10 stop | ETH | DOWN | 0.41 | 0.55 | 1.05 |
| 11-22 02:08 | +5 | ETH | DOWN | 0.41 | 0.55 | 1.05 |
| 11-22 02:07 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.71 |
| 11-22 02:07 | +10 stop | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 11-22 02:06 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-22 02:06 | +10 stop | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-22 02:06 | +15 | NEAR | UP | 0.63 | 0.88 | 2.25 |
| 11-22 02:06 | +10 | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-22 02:06 | +5 | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-22 02:06 | +5 | BTC | UP | 0.63 | 0.72 | 0.58 |
| 11-22 02:06 | +10 stop | ETH | UP | 0.66 | 0.51 | -1.84 |
| 11-22 02:06 | +10 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-22 02:06 | +5 | ETH | UP | 0.66 | 0.75 | 0.60 |
| 11-22 02:05 | +5 | BNB | UP | 0.61 | no | -6.27 |
| 11-22 02:05 | +10 stop | SOL | DOWN | 0.57 | 0.75 | 1.48 |
| 11-22 02:05 | +5 | BNB | UP | 0.52 | 0.58 | 0.24 |
| 11-22 02:04 | +10 stop | ZEC | UP | 0.62 | 0.47 | -1.85 |
| 11-22 02:04 | +10 stop | BTC | UP | 0.68 | 0.30 | -4.11 |
| 11-22 02:04 | +10 stop | DOGE | DOWN | 0.67 | 0.84 | 1.44 |
| 11-22 02:04 | +10 stop | XRP | UP | 0.59 | 0.42 | -2.01 |
| 11-22 02:04 | +10 | XRP | UP | 0.59 | no | -6.07 |
| 11-22 02:04 | +5 | XRP | UP | 0.58 | no | -5.98 |
| 11-22 02:04 | +10 stop | ETH | UP | 0.65 | 0.76 | 0.81 |
