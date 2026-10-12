# Range-Scalp Bot

*Updated Mon Oct 12 10:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13449 | 11637 | 1812 (25) | 3 | $-4276.56 | -5.0% |
| **+10¢** | 10184 | 8083 | 2101 (37) | 2 | $-3984.43 | -6.2% |
| **+15¢** | 8572 | 6326 | 2246 (55) | 2 | $-3495.60 | -6.5% |
| **+20¢** | 7631 | 5287 | 2344 (70) | 2 | $-2976.87 | -6.2% |
| **+10¢ (15¢ stop)** | 16548 | 16507 | 41 (25) | 1 | $-6458.17 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 10:39 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 10-12 10:39 | +5 | BTC | DOWN | 0.67 | open |  |
| 10-12 10:38 | +10 stop | HYPE | DOWN | 0.71 | 0.52 | -2.23 |
| 10-12 10:38 | +20 | HYPE | DOWN | 0.71 | open |  |
| 10-12 10:38 | +15 | HYPE | DOWN | 0.71 | open |  |
| 10-12 10:38 | +10 | HYPE | DOWN | 0.71 | open |  |
| 10-12 10:38 | +5 | HYPE | DOWN | 0.71 | open |  |
| 10-12 10:35 | +10 stop | BTC | UP | 0.60 | 0.40 | -2.34 |
| 10-12 10:35 | +20 | BTC | UP | 0.60 | open |  |
| 10-12 10:35 | +15 | BTC | UP | 0.60 | open |  |
| 10-12 10:35 | +10 | BTC | UP | 0.60 | open |  |
| 10-12 10:34 | +10 stop | ETH | UP | 0.58 | 0.69 | 0.77 |
| 10-12 10:34 | +10 stop | SOL | UP | 0.63 | 0.84 | 1.83 |
| 10-12 10:34 | +10 | XRP | UP | 0.64 | 0.75 | 0.79 |
| 10-12 10:32 | +5 | XRP | DOWN | 0.59 | open |  |
| 10-12 10:32 | +10 stop | SOL | DOWN | 0.61 | 0.46 | -1.85 |
| 10-12 10:31 | +10 stop | XRP | UP | 0.51 | 0.63 | 0.85 |
| 10-12 10:31 | +20 | XRP | UP | 0.51 | 0.75 | 2.08 |
| 10-12 10:31 | +15 | XRP | UP | 0.52 | 0.70 | 1.47 |
| 10-12 10:31 | +10 | XRP | UP | 0.49 | 0.60 | 0.75 |
| 10-12 10:31 | +5 | XRP | UP | 0.49 | 0.54 | 0.14 |
| 10-12 10:31 | +10 stop | BNB | UP | 0.68 | 0.83 | 1.24 |
| 10-12 10:31 | +20 | BNB | UP | 0.68 | 0.89 | 1.87 |
| 10-12 10:31 | +15 | BNB | UP | 0.68 | 0.83 | 1.24 |
| 10-12 10:31 | +10 | BNB | UP | 0.68 | 0.83 | 1.24 |
| 10-12 10:31 | +5 | BNB | UP | 0.68 | 0.73 | 0.20 |
| 10-12 10:31 | +10 stop | ZEC | UP | 0.63 | 0.74 | 0.79 |
| 10-12 10:31 | +20 | ZEC | UP | 0.63 | 0.83 | 1.73 |
| 10-12 10:31 | +15 | ZEC | UP | 0.63 | 0.83 | 1.73 |
| 10-12 10:31 | +10 | ZEC | UP | 0.63 | 0.74 | 0.79 |
| 10-12 10:31 | +5 | ZEC | UP | 0.63 | 0.74 | 0.79 |
| 10-12 10:31 | +5 | BTC | DOWN | 0.55 | 0.82 | 2.41 |
| 10-12 10:31 | +5 | ETH | UP | 0.55 | 0.61 | 0.25 |
| 10-12 10:30 | +10 stop | ETH | UP | 0.59 | 0.43 | -1.95 |
| 10-12 10:30 | +20 | ETH | UP | 0.59 | 0.83 | 2.13 |
| 10-12 10:30 | +15 | ETH | UP | 0.59 | 0.83 | 2.13 |
| 10-12 10:30 | +10 | ETH | UP | 0.59 | 0.69 | 0.68 |
| 10-12 10:30 | +5 | ETH | UP | 0.59 | 0.64 | 0.16 |
| 10-12 10:30 | +10 stop | SOL | UP | 0.61 | 0.44 | -2.05 |
| 10-12 10:30 | +20 | SOL | UP | 0.61 | 0.84 | 2.03 |
