# Range-Scalp Bot

*Updated Sat Nov 21 23:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67907 | 59272 | 8635 (138) | 3 | $-18151.64 | -4.2% |
| **+10¢** | 50705 | 40615 | 10090 (181) | 3 | $-16836.63 | -5.3% |
| **+15¢** | 42508 | 31630 | 10878 (230) | 3 | $-15095.49 | -5.7% |
| **+20¢** | 37838 | 26404 | 11434 (288) | 3 | $-13429.58 | -5.7% |
| **+10¢ (15¢ stop)** | 82668 | 82490 | 178 (110) | 3 | $-30346.75 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 23:16 | +10 stop | ETH | UP | 0.59 | open |  |
| 11-21 23:16 | +20 | ETH | UP | 0.59 | open |  |
| 11-21 23:16 | +15 | ETH | UP | 0.59 | open |  |
| 11-21 23:16 | +10 | ETH | UP | 0.59 | open |  |
| 11-21 23:16 | +5 | ETH | UP | 0.59 | open |  |
| 11-21 23:16 | +10 stop | ZEC | UP | 0.58 | open |  |
| 11-21 23:16 | +20 | ZEC | UP | 0.58 | open |  |
| 11-21 23:16 | +15 | ZEC | UP | 0.58 | open |  |
| 11-21 23:16 | +10 | ZEC | UP | 0.58 | open |  |
| 11-21 23:16 | +5 | ZEC | UP | 0.58 | open |  |
| 11-21 23:16 | +10 stop | HYPE | UP | 0.68 | open |  |
| 11-21 23:16 | +20 | HYPE | UP | 0.68 | open |  |
| 11-21 23:16 | +15 | HYPE | UP | 0.68 | open |  |
| 11-21 23:16 | +10 | HYPE | UP | 0.68 | open |  |
| 11-21 23:16 | +5 | HYPE | UP | 0.68 | open |  |
| 11-21 23:09 | +10 stop | HYPE | DOWN | 0.58 | 0.33 | -2.80 |
| 11-21 23:07 | +10 stop | BNB | UP | 0.63 | 0.74 | 0.78 |
| 11-21 23:06 | +5 | DOGE | UP | 0.68 | 0.78 | 0.72 |
| 11-21 23:06 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-21 23:06 | +5 | SOL | UP | 0.69 | 0.77 | 0.52 |
| 11-21 23:06 | +10 stop | ETH | UP | 0.65 | 0.80 | 1.22 |
| 11-21 23:05 | +10 stop | SOL | UP | 0.71 | 0.83 | 0.97 |
| 11-21 23:05 | +10 stop | NEAR | UP | 0.71 | 0.82 | 0.87 |
| 11-21 23:05 | +10 stop | HYPE | DOWN | 0.66 | 0.45 | -2.44 |
| 11-21 23:05 | +15 | HYPE | DOWN | 0.66 | yes | -6.76 |
| 11-21 23:05 | +10 | HYPE | DOWN | 0.66 | yes | -6.76 |
| 11-21 23:05 | +5 | HYPE | DOWN | 0.66 | yes | -6.76 |
| 11-21 23:04 | +10 stop | XRP | UP | 0.67 | 0.77 | 0.71 |
| 11-21 23:04 | +10 stop | BTC | DOWN | 0.65 | 0.49 | -1.94 |
| 11-21 23:04 | +10 | BTC | DOWN | 0.65 | yes | -6.66 |
| 11-21 23:04 | +5 | BTC | DOWN | 0.65 | yes | -6.66 |
| 11-21 23:04 | +10 stop | DOGE | DOWN | 0.68 | 0.48 | -2.34 |
| 11-21 23:04 | +10 stop | ETH | DOWN | 0.60 | 0.42 | -2.15 |
| 11-21 23:04 | +20 | ETH | DOWN | 0.60 | yes | -6.17 |
| 11-21 23:04 | +15 | ETH | DOWN | 0.60 | yes | -6.17 |
| 11-21 23:04 | +10 | ETH | DOWN | 0.60 | yes | -6.17 |
| 11-21 23:04 | +5 | ETH | DOWN | 0.60 | yes | -6.17 |
| 11-21 23:04 | +10 stop | BNB | DOWN | 0.62 | 0.45 | -2.03 |
| 11-21 23:04 | +10 stop | NEAR | DOWN | 0.63 | 0.46 | -2.04 |
| 11-21 23:03 | +10 stop | SOL | DOWN | 0.52 | 0.36 | -1.95 |
