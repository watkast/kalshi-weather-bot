# Range-Scalp Bot

*Updated Sat Nov 14 10:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59326 | 51772 | 7554 (107) | 3 | $-15965.70 | -4.3% |
| **+10¢** | 44307 | 35465 | 8842 (140) | 4 | $-14998.23 | -5.4% |
| **+15¢** | 37131 | 27596 | 9535 (176) | 5 | $-13629.04 | -5.9% |
| **+20¢** | 33076 | 23066 | 10010 (228) | 6 | $-12019.49 | -5.8% |
| **+10¢ (15¢ stop)** | 72171 | 72029 | 142 (82) | 1 | $-26527.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 10:28 | +10 stop | SOL | DOWN | 0.59 | open |  |
| 11-14 10:28 | +10 stop | HYPE | UP | 0.67 | 0.82 | 1.23 |
| 11-14 10:28 | +5 | HYPE | UP | 0.67 | 0.82 | 1.23 |
| 11-14 10:27 | +10 stop | ETH | UP | 0.56 | 0.73 | 1.38 |
| 11-14 10:27 | +5 | ETH | UP | 0.56 | 0.61 | 0.15 |
| 11-14 10:27 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 11-14 10:27 | +5 | BTC | UP | 0.59 | 0.69 | 0.68 |
| 11-14 10:26 | +10 stop | SOL | DOWN | 0.71 | 0.56 | -1.83 |
| 11-14 10:26 | +10 stop | BTC | UP | 0.49 | 0.62 | 0.95 |
| 11-14 10:26 | +5 | BTC | UP | 0.49 | 0.62 | 0.95 |
| 11-14 10:25 | +10 stop | HYPE | DOWN | 0.55 | 0.39 | -1.95 |
| 11-14 10:25 | +10 stop | BTC | UP | 0.51 | 0.65 | 1.06 |
| 11-14 10:25 | +5 | BTC | UP | 0.52 | 0.65 | 0.96 |
| 11-14 10:23 | +10 stop | XRP | UP | 0.70 | 0.86 | 1.36 |
| 11-14 10:23 | +10 stop | ETH | UP | 0.67 | 0.45 | -2.54 |
| 11-14 10:23 | +10 stop | SOL | DOWN | 0.70 | 0.48 | -2.53 |
| 11-14 10:23 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-14 10:23 | +15 | SOL | DOWN | 0.70 | open |  |
| 11-14 10:23 | +10 | SOL | DOWN | 0.70 | open |  |
| 11-14 10:23 | +10 stop | BNB | UP | 0.68 | 0.78 | 0.71 |
| 11-14 10:23 | +20 | BNB | UP | 0.68 | 0.91 | 2.08 |
| 11-14 10:23 | +15 | BNB | UP | 0.68 | 0.87 | 1.66 |
| 11-14 10:23 | +10 | BNB | UP | 0.68 | 0.78 | 0.71 |
| 11-14 10:23 | +5 | BNB | UP | 0.68 | 0.74 | 0.30 |
| 11-14 10:23 | +10 stop | BTC | UP | 0.70 | 0.82 | 0.94 |
| 11-14 10:23 | +5 | BTC | UP | 0.70 | 0.77 | 0.42 |
| 11-14 10:22 | +15 | BNB | DOWN | 0.41 | 0.68 | 2.37 |
| 11-14 10:22 | +15 | ETH | DOWN | 0.48 | open |  |
| 11-14 10:22 | +10 stop | BNB | DOWN | 0.42 | 0.68 | 2.26 |
| 11-14 10:22 | +10 | BNB | DOWN | 0.42 | 0.68 | 2.26 |
| 11-14 10:22 | +5 | BNB | DOWN | 0.42 | 0.68 | 2.26 |
| 11-14 10:22 | +10 stop | ETH | DOWN | 0.61 | 0.39 | -2.54 |
| 11-14 10:22 | +10 | ETH | DOWN | 0.61 | open |  |
| 11-14 10:22 | +10 stop | BNB | UP | 0.33 | 0.55 | 1.86 |
| 11-14 10:22 | +10 | BNB | UP | 0.33 | 0.55 | 1.86 |
| 11-14 10:22 | +5 | BNB | UP | 0.33 | 0.55 | 1.86 |
| 11-14 10:22 | +10 stop | XRP | DOWN | 0.69 | 0.53 | -1.93 |
| 11-14 10:21 | +20 | XRP | UP | 0.71 | 0.94 | 2.12 |
| 11-14 10:21 | +15 | XRP | UP | 0.71 | 0.86 | 1.26 |
| 11-14 10:21 | +10 stop | DOGE | UP | 0.67 | 0.45 | -2.54 |
