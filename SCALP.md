# Range-Scalp Bot

*Updated Fri Oct 09 09:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8849 | 7654 | 1195 (13) | 4 | $-2902.51 | -5.2% |
| **+10¢** | 6704 | 5300 | 1404 (25) | 5 | $-2795.27 | -6.6% |
| **+15¢** | 5655 | 4176 | 1479 (37) | 5 | $-2273.54 | -6.4% |
| **+20¢** | 5034 | 3498 | 1536 (45) | 6 | $-1876.65 | -5.9% |
| **+10¢ (15¢ stop)** | 10795 | 10765 | 30 (19) | 3 | $-4032.98 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 09:21 | +10 stop | HYPE | DOWN | 0.59 | open |  |
| 10-09 09:21 | +10 stop | BNB | DOWN | 0.66 | open |  |
| 10-09 09:21 | +10 | BNB | DOWN | 0.66 | open |  |
| 10-09 09:21 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-09 09:21 | +10 stop | BTC | UP | 0.59 | open |  |
| 10-09 09:21 | +5 | HYPE | DOWN | 0.58 | 0.63 | 0.15 |
| 10-09 09:20 | +10 stop | HYPE | DOWN | 0.71 | 0.50 | -2.43 |
| 10-09 09:20 | +10 stop | SOL | UP | 0.56 | 0.66 | 0.66 |
| 10-09 09:20 | +10 stop | XRP | DOWN | 0.70 | 0.82 | 0.90 |
| 10-09 09:19 | +10 stop | XRP | UP | 0.61 | 0.36 | -2.84 |
| 10-09 09:18 | +10 stop | HYPE | UP | 0.66 | 0.43 | -2.68 |
| 10-09 09:18 | +10 stop | BNB | DOWN | 0.53 | 0.66 | 0.96 |
| 10-09 09:18 | +10 stop | DOGE | DOWN | 0.56 | 0.69 | 0.95 |
| 10-09 09:18 | +20 | DOGE | DOWN | 0.56 | 0.86 | 2.71 |
| 10-09 09:18 | +15 | DOGE | DOWN | 0.56 | 0.74 | 1.46 |
| 10-09 09:18 | +10 | DOGE | DOWN | 0.56 | 0.69 | 0.96 |
| 10-09 09:18 | +5 | DOGE | DOWN | 0.56 | 0.66 | 0.65 |
| 10-09 09:18 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-09 09:18 | +10 stop | BTC | UP | 0.62 | 0.41 | -2.44 |
| 10-09 09:16 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-09 09:16 | +20 | ZEC | DOWN | 0.70 | open |  |
| 10-09 09:16 | +15 | ZEC | DOWN | 0.70 | 0.86 | 1.36 |
| 10-09 09:16 | +10 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-09 09:16 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.52 |
| 10-09 09:16 | +10 stop | BNB | DOWN | 0.66 | 0.51 | -1.87 |
| 10-09 09:16 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-09 09:16 | +15 | BNB | DOWN | 0.66 | open |  |
| 10-09 09:16 | +10 | BNB | DOWN | 0.66 | 0.78 | 0.88 |
| 10-09 09:16 | +5 | BNB | DOWN | 0.66 | 0.78 | 0.88 |
| 10-09 09:16 | +10 stop | BTC | DOWN | 0.62 | 0.43 | -2.25 |
| 10-09 09:16 | +20 | BTC | DOWN | 0.62 | open |  |
| 10-09 09:16 | +15 | BTC | DOWN | 0.62 | open |  |
| 10-09 09:16 | +10 | BTC | DOWN | 0.62 | open |  |
| 10-09 09:16 | +5 | BTC | DOWN | 0.62 | open |  |
| 10-09 09:16 | +10 stop | ETH | DOWN | 0.63 | 0.22 | -4.40 |
| 10-09 09:16 | +20 | ETH | DOWN | 0.63 | open |  |
| 10-09 09:16 | +15 | ETH | DOWN | 0.63 | open |  |
| 10-09 09:16 | +10 | ETH | DOWN | 0.63 | open |  |
| 10-09 09:16 | +5 | ETH | DOWN | 0.63 | open |  |
| 10-09 09:16 | +10 stop | SOL | DOWN | 0.64 | 0.49 | -1.85 |
