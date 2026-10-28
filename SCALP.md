# Range-Scalp Bot

*Updated Wed Oct 28 13:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38159 | 33294 | 4865 (46) | 5 | $-10763.09 | -4.5% |
| **+10¢** | 28463 | 22838 | 5625 (68) | 6 | $-9595.90 | -5.4% |
| **+15¢** | 23812 | 17773 | 6039 (93) | 6 | $-8543.17 | -5.7% |
| **+20¢** | 21121 | 14796 | 6325 (118) | 7 | $-7514.59 | -5.7% |
| **+10¢ (15¢ stop)** | 46719 | 46652 | 67 (35) | 2 | $-17768.37 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 13:24 | +5 | DOGE | DOWN | 0.54 | 0.59 | 0.15 |
| 10-28 13:22 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-28 13:21 | +10 stop | ETH | DOWN | 0.58 | 0.70 | 0.87 |
| 10-28 13:21 | +10 stop | XRP | UP | 0.62 | 0.43 | -2.25 |
| 10-28 13:21 | +10 | XRP | UP | 0.62 | open |  |
| 10-28 13:21 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-28 13:20 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.26 |
| 10-28 13:19 | +10 stop | DOGE | DOWN | 0.63 | open |  |
| 10-28 13:19 | +10 | DOGE | DOWN | 0.63 | open |  |
| 10-28 13:19 | +5 | DOGE | DOWN | 0.63 | 0.68 | 0.17 |
| 10-28 13:19 | +5 | SOL | DOWN | 0.59 | 0.68 | 0.57 |
| 10-28 13:18 | +10 stop | BTC | DOWN | 0.56 | 0.75 | 1.58 |
| 10-28 13:18 | +10 stop | XRP | DOWN | 0.55 | 0.35 | -2.34 |
| 10-28 13:18 | +10 stop | ETH | DOWN | 0.62 | 0.46 | -1.95 |
| 10-28 13:18 | +5 | XRP | DOWN | 0.55 | open |  |
| 10-28 13:17 | +10 stop | NEAR | DOWN | 0.68 | open |  |
| 10-28 13:17 | +20 | NEAR | DOWN | 0.68 | open |  |
| 10-28 13:17 | +15 | NEAR | DOWN | 0.68 | open |  |
| 10-28 13:17 | +10 | NEAR | DOWN | 0.68 | open |  |
| 10-28 13:17 | +5 | NEAR | DOWN | 0.68 | open |  |
| 10-28 13:17 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-28 13:17 | +20 | SOL | DOWN | 0.67 | open |  |
| 10-28 13:17 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 10-28 13:17 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-28 13:17 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.61 |
| 10-28 13:17 | +10 stop | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-28 13:17 | +20 | DOGE | DOWN | 0.67 | open |  |
| 10-28 13:17 | +15 | DOGE | DOWN | 0.67 | open |  |
| 10-28 13:17 | +10 | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-28 13:17 | +5 | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-28 13:17 | +10 stop | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-28 13:17 | +20 | BNB | DOWN | 0.63 | 0.84 | 1.83 |
| 10-28 13:17 | +15 | BNB | DOWN | 0.63 | 0.84 | 1.83 |
| 10-28 13:17 | +10 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-28 13:17 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 10-28 13:16 | +10 stop | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-28 13:16 | +20 | HYPE | DOWN | 0.61 | 0.84 | 2.03 |
| 10-28 13:16 | +15 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-28 13:16 | +10 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-28 13:16 | +5 | HYPE | DOWN | 0.60 | 0.69 | 0.58 |
