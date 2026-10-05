# Range-Scalp Bot

*Updated Mon Oct 05 18:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4099 | 3522 | 577 (4) | 2 | $-1487.35 | -5.7% |
| **+10¢** | 3167 | 2505 | 662 (5) | 2 | $-1345.58 | -6.7% |
| **+15¢** | 2661 | 1964 | 697 (8) | 5 | $-1155.84 | -6.9% |
| **+20¢** | 2374 | 1648 | 726 (13) | 7 | $-991.26 | -6.6% |
| **+10¢ (15¢ stop)** | 5059 | 5054 | 5 (2) | 0 | $-1863.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 18:17 | +5 | NEAR | UP | 0.63 | 0.68 | 0.17 |
| 10-05 18:16 | +10 stop | SOL | UP | 0.59 | 0.77 | 1.50 |
| 10-05 18:16 | +20 | SOL | UP | 0.59 | 0.81 | 1.92 |
| 10-05 18:16 | +15 | SOL | UP | 0.59 | 0.77 | 1.50 |
| 10-05 18:16 | +10 | SOL | UP | 0.59 | 0.77 | 1.50 |
| 10-05 18:16 | +5 | SOL | UP | 0.59 | 0.66 | 0.37 |
| 10-05 18:16 | +10 stop | NEAR | UP | 0.56 | 0.66 | 0.66 |
| 10-05 18:16 | +20 | NEAR | UP | 0.56 | open |  |
| 10-05 18:16 | +15 | NEAR | UP | 0.57 | open |  |
| 10-05 18:16 | +10 | NEAR | UP | 0.57 | 0.68 | 0.76 |
| 10-05 18:16 | +5 | NEAR | UP | 0.59 | 0.64 | 0.16 |
| 10-05 18:16 | +10 stop | BTC | UP | 0.57 | 0.72 | 1.17 |
| 10-05 18:16 | +20 | BTC | UP | 0.57 | open |  |
| 10-05 18:16 | +15 | BTC | UP | 0.57 | 0.72 | 1.17 |
| 10-05 18:16 | +10 | BTC | UP | 0.57 | 0.72 | 1.17 |
| 10-05 18:16 | +5 | BTC | UP | 0.57 | 0.65 | 0.46 |
| 10-05 18:16 | +10 stop | ETH | UP | 0.63 | 0.76 | 1.00 |
| 10-05 18:16 | +20 | ETH | UP | 0.63 | open |  |
| 10-05 18:16 | +15 | ETH | UP | 0.63 | open |  |
| 10-05 18:16 | +10 | ETH | UP | 0.63 | 0.76 | 1.00 |
| 10-05 18:16 | +5 | ETH | UP | 0.63 | 0.76 | 1.00 |
| 10-05 18:16 | +10 stop | HYPE | UP | 0.62 | 0.46 | -1.95 |
| 10-05 18:16 | +20 | HYPE | UP | 0.62 | open |  |
| 10-05 18:16 | +15 | HYPE | UP | 0.62 | open |  |
| 10-05 18:16 | +10 | HYPE | UP | 0.62 | open |  |
| 10-05 18:16 | +5 | HYPE | UP | 0.62 | open |  |
| 10-05 18:16 | +10 stop | ZEC | DOWN | 0.58 | 0.42 | -1.96 |
| 10-05 18:16 | +20 | ZEC | DOWN | 0.58 | open |  |
| 10-05 18:16 | +15 | ZEC | DOWN | 0.58 | open |  |
| 10-05 18:16 | +10 | ZEC | DOWN | 0.58 | open |  |
| 10-05 18:16 | +5 | ZEC | DOWN | 0.58 | open |  |
| 10-05 18:16 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 10-05 18:16 | +20 | XRP | UP | 0.68 | open |  |
| 10-05 18:16 | +15 | XRP | UP | 0.68 | open |  |
| 10-05 18:16 | +10 | XRP | UP | 0.68 | 0.78 | 0.71 |
| 10-05 18:16 | +5 | XRP | UP | 0.68 | 0.78 | 0.71 |
| 10-05 18:16 | +10 stop | DOGE | UP | 0.69 | 0.85 | 1.36 |
| 10-05 18:16 | +20 | DOGE | UP | 0.69 | open |  |
| 10-05 18:16 | +15 | DOGE | UP | 0.69 | 0.85 | 1.36 |
| 10-05 18:16 | +10 | DOGE | UP | 0.69 | 0.85 | 1.36 |
