# Range-Scalp Bot

*Updated Wed Oct 07 22:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6885 | 5980 | 905 (10) | 2 | $-2068.11 | -4.8% |
| **+10¢** | 5222 | 4161 | 1061 (17) | 2 | $-1948.03 | -5.9% |
| **+15¢** | 4375 | 3259 | 1116 (21) | 4 | $-1614.77 | -5.9% |
| **+20¢** | 3908 | 2745 | 1163 (28) | 6 | $-1281.19 | -5.2% |
| **+10¢ (15¢ stop)** | 8333 | 8316 | 17 (10) | 1 | $-2955.72 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 22:04 | +10 stop | SOL | UP | 0.63 | 0.74 | 0.79 |
| 10-07 22:04 | +20 | SOL | UP | 0.64 | open |  |
| 10-07 22:04 | +15 | SOL | UP | 0.64 | open |  |
| 10-07 22:04 | +10 | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-07 22:04 | +5 | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-07 22:04 | +10 stop | BTC | UP | 0.68 | 0.80 | 0.92 |
| 10-07 22:04 | +20 | BTC | UP | 0.68 | open |  |
| 10-07 22:04 | +15 | BTC | UP | 0.68 | open |  |
| 10-07 22:04 | +10 | BTC | UP | 0.68 | 0.80 | 0.92 |
| 10-07 22:04 | +5 | BTC | UP | 0.68 | 0.74 | 0.30 |
| 10-07 22:04 | +10 | ETH | DOWN | 0.71 | open |  |
| 10-07 22:04 | +5 | ETH | DOWN | 0.71 | open |  |
| 10-07 22:04 | +10 stop | XRP | UP | 0.65 | 0.79 | 1.11 |
| 10-07 22:04 | +20 | XRP | UP | 0.65 | open |  |
| 10-07 22:04 | +15 | XRP | UP | 0.65 | 0.81 | 1.32 |
| 10-07 22:04 | +10 | XRP | UP | 0.65 | 0.79 | 1.12 |
| 10-07 22:04 | +5 | XRP | UP | 0.65 | 0.79 | 1.12 |
| 10-07 22:03 | +10 stop | DOGE | UP | 0.67 | open |  |
| 10-07 22:03 | +10 | DOGE | UP | 0.67 | open |  |
| 10-07 22:03 | +5 | DOGE | UP | 0.68 | open |  |
| 10-07 22:03 | +10 stop | ETH | UP | 0.47 | 0.30 | -2.03 |
| 10-07 22:03 | +20 | ETH | UP | 0.47 | open |  |
| 10-07 22:03 | +15 | ETH | UP | 0.47 | open |  |
| 10-07 22:03 | +10 | ETH | UP | 0.45 | 0.56 | 0.74 |
| 10-07 22:03 | +5 | ETH | UP | 0.45 | 0.54 | 0.54 |
| 10-07 22:03 | +10 stop | ZEC | UP | 0.61 | 0.75 | 1.12 |
| 10-07 22:03 | +20 | ZEC | UP | 0.58 | 0.81 | 2.01 |
| 10-07 22:03 | +15 | ZEC | UP | 0.58 | 0.75 | 1.38 |
| 10-07 22:03 | +10 | ZEC | UP | 0.58 | 0.75 | 1.38 |
| 10-07 22:03 | +5 | ZEC | UP | 0.61 | 0.75 | 1.09 |
| 10-07 22:02 | +10 stop | DOGE | UP | 0.56 | 0.66 | 0.66 |
| 10-07 22:02 | +20 | DOGE | UP | 0.57 | open |  |
| 10-07 22:02 | +15 | DOGE | UP | 0.57 | open |  |
| 10-07 22:02 | +10 | DOGE | UP | 0.56 | 0.66 | 0.66 |
| 10-07 22:02 | +5 | DOGE | UP | 0.55 | 0.61 | 0.25 |
| 10-07 22:00 | +10 stop | HYPE | UP | 0.65 | 0.77 | 0.91 |
| 10-07 22:00 | +20 | HYPE | UP | 0.65 | open |  |
| 10-07 22:00 | +15 | HYPE | UP | 0.65 | 0.82 | 1.39 |
| 10-07 22:00 | +10 | HYPE | UP | 0.63 | 0.77 | 1.10 |
| 10-07 22:00 | +5 | HYPE | UP | 0.63 | 0.77 | 1.10 |
