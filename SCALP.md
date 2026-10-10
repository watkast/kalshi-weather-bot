# Range-Scalp Bot

*Updated Sat Oct 10 00:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9693 | 8368 | 1325 (18) | 2 | $-3256.49 | -5.3% |
| **+10¢** | 7321 | 5772 | 1549 (30) | 4 | $-3140.77 | -6.8% |
| **+15¢** | 6169 | 4535 | 1634 (43) | 6 | $-2611.98 | -6.7% |
| **+20¢** | 5486 | 3788 | 1698 (55) | 8 | $-2181.89 | -6.3% |
| **+10¢ (15¢ stop)** | 11864 | 11829 | 35 (22) | 2 | $-4563.13 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 00:19 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 10-10 00:19 | +10 | BTC | DOWN | 0.67 | open |  |
| 10-10 00:19 | +5 | BTC | DOWN | 0.67 | open |  |
| 10-10 00:19 | +10 stop | DOGE | DOWN | 0.41 | 0.55 | 1.05 |
| 10-10 00:19 | +15 | DOGE | DOWN | 0.42 | open |  |
| 10-10 00:19 | +10 stop | ZEC | DOWN | 0.48 | 0.30 | -2.13 |
| 10-10 00:19 | +10 | ZEC | DOWN | 0.48 | open |  |
| 10-10 00:19 | +5 | ZEC | DOWN | 0.45 | open |  |
| 10-10 00:19 | +10 stop | SOL | DOWN | 0.71 | 0.47 | -2.73 |
| 10-10 00:19 | +10 | SOL | DOWN | 0.71 | open |  |
| 10-10 00:18 | +5 | HYPE | UP | 0.63 | 0.76 | 1.00 |
| 10-10 00:17 | +10 stop | DOGE | UP | 0.64 | 0.39 | -2.84 |
| 10-10 00:17 | +10 | DOGE | UP | 0.64 | 0.86 | 1.94 |
| 10-10 00:17 | +5 | DOGE | UP | 0.65 | 0.70 | 0.19 |
| 10-10 00:17 | +10 stop | BNB | UP | 0.64 | 0.49 | -1.85 |
| 10-10 00:17 | +10 | BNB | UP | 0.64 | 0.82 | 1.47 |
| 10-10 00:17 | +5 | BNB | UP | 0.64 | 0.82 | 1.52 |
| 10-10 00:16 | +5 | SOL | UP | 0.55 | 0.63 | 0.45 |
| 10-10 00:16 | +10 stop | ETH | UP | 0.68 | 0.48 | -2.34 |
| 10-10 00:16 | +15 | ETH | UP | 0.68 | open |  |
| 10-10 00:16 | +10 | ETH | UP | 0.68 | 0.78 | 0.71 |
| 10-10 00:16 | +5 | ETH | UP | 0.69 | 0.78 | 0.62 |
| 10-10 00:16 | +10 stop | XRP | UP | 0.67 | 0.82 | 1.23 |
| 10-10 00:16 | +20 | XRP | UP | 0.67 | open |  |
| 10-10 00:16 | +15 | XRP | UP | 0.68 | open |  |
| 10-10 00:16 | +10 | XRP | UP | 0.68 | 0.82 | 1.13 |
| 10-10 00:16 | +5 | XRP | UP | 0.69 | 0.76 | 0.42 |
| 10-10 00:15 | +10 stop | BTC | DOWN | 0.55 | 0.69 | 1.07 |
| 10-10 00:15 | +20 | BTC | DOWN | 0.55 | open |  |
| 10-10 00:15 | +15 | BTC | DOWN | 0.55 | open |  |
| 10-10 00:15 | +10 | BTC | DOWN | 0.56 | 0.69 | 0.97 |
| 10-10 00:15 | +5 | BTC | DOWN | 0.56 | 0.69 | 0.97 |
| 10-10 00:15 | +10 stop | HYPE | UP | 0.70 | open |  |
| 10-10 00:15 | +20 | HYPE | UP | 0.70 | open |  |
| 10-10 00:15 | +15 | HYPE | UP | 0.70 | open |  |
| 10-10 00:15 | +10 | HYPE | UP | 0.70 | open |  |
| 10-10 00:15 | +5 | HYPE | UP | 0.70 | 0.76 | 0.28 |
| 10-10 00:15 | +10 stop | SOL | DOWN | 0.48 | 0.62 | 1.05 |
| 10-10 00:15 | +20 | SOL | DOWN | 0.49 | 0.69 | 1.67 |
| 10-10 00:15 | +15 | SOL | DOWN | 0.48 | 0.69 | 1.77 |
