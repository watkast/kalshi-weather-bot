# Range-Scalp Bot

*Updated Wed Oct 28 22:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38584 | 33666 | 4918 (48) | 0 | $-10871.97 | -4.5% |
| **+10¢** | 28778 | 23096 | 5682 (70) | 0 | $-9660.82 | -5.3% |
| **+15¢** | 24073 | 17969 | 6104 (95) | 0 | $-8632.93 | -5.7% |
| **+20¢** | 21356 | 14966 | 6390 (120) | 0 | $-7556.50 | -5.6% |
| **+10¢ (15¢ stop)** | 47192 | 47125 | 67 (35) | 0 | $-17908.71 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 22:01 | +10 stop | BTC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-28 22:01 | +20 | BTC | DOWN | 0.60 | 0.85 | 2.24 |
| 10-28 22:01 | +15 | BTC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-28 22:01 | +10 | BTC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-28 22:01 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-28 22:01 | +10 stop | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 10-28 22:01 | +20 | DOGE | DOWN | 0.70 | 0.91 | 1.86 |
| 10-28 22:01 | +15 | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 10-28 22:01 | +10 | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 10-28 22:01 | +5 | DOGE | DOWN | 0.70 | 0.78 | 0.52 |
| 10-28 22:01 | +10 stop | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-28 22:01 | +20 | ETH | DOWN | 0.66 | 0.90 | 2.20 |
| 10-28 22:01 | +15 | ETH | DOWN | 0.66 | 0.83 | 1.44 |
| 10-28 22:01 | +10 | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-28 22:01 | +5 | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-28 21:42 | +5 | DOGE | UP | 0.69 | 0.77 | 0.52 |
| 10-28 21:42 | +10 stop | ZEC | UP | 0.59 | 0.40 | -2.24 |
| 10-28 21:42 | +10 stop | HYPE | UP | 0.56 | 0.75 | 1.58 |
| 10-28 21:42 | +10 stop | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-28 21:41 | +10 stop | BTC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-28 21:41 | +15 | BTC | DOWN | 0.55 | yes | -5.68 |
| 10-28 21:41 | +10 | BTC | DOWN | 0.56 | yes | -5.78 |
| 10-28 21:41 | +5 | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 10-28 21:40 | +10 stop | ETH | UP | 0.47 | 0.68 | 1.76 |
| 10-28 21:40 | +10 | ETH | UP | 0.47 | 0.68 | 1.76 |
| 10-28 21:40 | +5 | ETH | UP | 0.47 | 0.68 | 1.76 |
| 10-28 21:40 | +10 stop | BNB | UP | 0.68 | 0.51 | -2.01 |
| 10-28 21:40 | +10 stop | DOGE | UP | 0.60 | 0.44 | -1.95 |
| 10-28 21:40 | +10 | DOGE | UP | 0.60 | 0.77 | 1.40 |
| 10-28 21:40 | +5 | DOGE | UP | 0.60 | 0.65 | 0.17 |
| 10-28 21:40 | +10 stop | BTC | DOWN | 0.46 | 0.64 | 1.45 |
| 10-28 21:40 | +15 | BTC | DOWN | 0.46 | 0.64 | 1.45 |
| 10-28 21:40 | +10 | BTC | DOWN | 0.46 | 0.64 | 1.45 |
| 10-28 21:40 | +5 | BTC | DOWN | 0.50 | 0.55 | 0.14 |
| 10-28 21:40 | +10 stop | HYPE | DOWN | 0.63 | 0.48 | -1.85 |
| 10-28 21:40 | +10 | HYPE | DOWN | 0.63 | yes | -6.47 |
| 10-28 21:40 | +5 | HYPE | DOWN | 0.63 | yes | -6.47 |
| 10-28 21:40 | +10 stop | ETH | DOWN | 0.42 | 0.55 | 0.94 |
| 10-28 21:40 | +10 | ETH | DOWN | 0.42 | 0.55 | 0.94 |
| 10-28 21:40 | +5 | ETH | DOWN | 0.42 | 0.55 | 0.94 |
