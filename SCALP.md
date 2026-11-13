# Range-Scalp Bot

*Updated Fri Nov 13 21:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58687 | 51211 | 7476 (105) | 3 | $-15813.41 | -4.3% |
| **+10¢** | 43837 | 35093 | 8744 (139) | 4 | $-14784.85 | -5.4% |
| **+15¢** | 36739 | 27320 | 9419 (174) | 5 | $-13365.91 | -5.8% |
| **+20¢** | 32730 | 22841 | 9889 (225) | 6 | $-11756.18 | -5.7% |
| **+10¢ (15¢ stop)** | 71453 | 71319 | 134 (82) | 4 | $-26295.92 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 21:32 | +10 stop | XRP | DOWN | 0.60 | open |  |
| 11-13 21:32 | +5 | ETH | DOWN | 0.70 | open |  |
| 11-13 21:32 | +10 stop | DOGE | DOWN | 0.70 | open |  |
| 11-13 21:32 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-13 21:32 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-13 21:32 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-13 21:32 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-13 21:32 | +10 stop | SOL | DOWN | 0.62 | open |  |
| 11-13 21:32 | +20 | SOL | DOWN | 0.62 | open |  |
| 11-13 21:32 | +15 | SOL | DOWN | 0.62 | open |  |
| 11-13 21:32 | +10 | SOL | DOWN | 0.62 | open |  |
| 11-13 21:32 | +5 | SOL | DOWN | 0.61 | open |  |
| 11-13 21:31 | +10 stop | XRP | UP | 0.56 | 0.40 | -1.94 |
| 11-13 21:31 | +20 | XRP | UP | 0.56 | open |  |
| 11-13 21:31 | +15 | XRP | UP | 0.57 | open |  |
| 11-13 21:31 | +10 | XRP | UP | 0.56 | open |  |
| 11-13 21:31 | +5 | XRP | UP | 0.56 | open |  |
| 11-13 21:31 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 11-13 21:31 | +20 | BNB | DOWN | 0.64 | open |  |
| 11-13 21:31 | +15 | BNB | DOWN | 0.64 | 0.81 | 1.43 |
| 11-13 21:31 | +10 | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-13 21:31 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 11-13 21:31 | +10 stop | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 11-13 21:31 | +20 | ETH | DOWN | 0.58 | open |  |
| 11-13 21:31 | +15 | ETH | DOWN | 0.59 | open |  |
| 11-13 21:31 | +10 | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 11-13 21:31 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 11-13 21:31 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 11-13 21:31 | +20 | BTC | DOWN | 0.70 | open |  |
| 11-13 21:31 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-13 21:31 | +10 | BTC | DOWN | 0.70 | open |  |
| 11-13 21:31 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-13 21:26 | +10 | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 11-13 21:26 | +5 | HYPE | UP | 0.68 | 0.79 | 0.87 |
| 11-13 21:25 | +10 stop | HYPE | UP | 0.65 | 0.79 | 1.12 |
| 11-13 21:25 | +5 | HYPE | UP | 0.63 | 0.68 | 0.17 |
| 11-13 21:24 | +10 stop | HYPE | DOWN | 0.51 | 0.36 | -1.85 |
| 11-13 21:24 | +5 | HYPE | DOWN | 0.53 | 0.58 | 0.14 |
| 11-13 21:22 | +5 | HYPE | DOWN | 0.69 | 0.82 | 0.99 |
| 11-13 21:21 | +10 stop | HYPE | DOWN | 0.57 | 0.82 | 2.21 |
