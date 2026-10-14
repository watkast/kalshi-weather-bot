# Range-Scalp Bot

*Updated Wed Oct 14 14:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16108 | 13954 | 2154 (27) | 1 | $-5099.56 | -5.0% |
| **+10¢** | 12174 | 9679 | 2495 (39) | 1 | $-4703.61 | -6.1% |
| **+15¢** | 10238 | 7557 | 2681 (58) | 1 | $-4224.19 | -6.6% |
| **+20¢** | 9107 | 6295 | 2812 (75) | 1 | $-3742.70 | -6.5% |
| **+10¢ (15¢ stop)** | 19833 | 19783 | 50 (29) | 0 | $-7624.72 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 14:38 | +10 stop | BTC | DOWN | 0.59 | 0.70 | 0.78 |
| 10-14 14:36 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-14 14:36 | +10 stop | ETH | DOWN | 0.60 | 0.71 | 0.78 |
| 10-14 14:36 | +5 | ETH | DOWN | 0.60 | 0.68 | 0.47 |
| 10-14 14:36 | +10 stop | DOGE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-14 14:35 | +10 stop | BTC | UP | 0.53 | 0.38 | -1.85 |
| 10-14 14:35 | +15 | BTC | UP | 0.53 | open |  |
| 10-14 14:35 | +10 | BTC | UP | 0.53 | open |  |
| 10-14 14:35 | +5 | BTC | UP | 0.53 | open |  |
| 10-14 14:35 | +10 stop | HYPE | UP | 0.54 | 0.38 | -1.95 |
| 10-14 14:35 | +5 | ETH | UP | 0.55 | 0.61 | 0.25 |
| 10-14 14:35 | +10 stop | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 10-14 14:35 | +20 | XRP | DOWN | 0.63 | 0.83 | 1.73 |
| 10-14 14:35 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 10-14 14:35 | +10 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 10-14 14:35 | +5 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
| 10-14 14:33 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 10-14 14:33 | +5 | NEAR | DOWN | 0.58 | 0.63 | 0.15 |
| 10-14 14:33 | +5 | BNB | DOWN | 0.59 | 0.68 | 0.57 |
| 10-14 14:32 | +10 stop | HYPE | DOWN | 0.62 | 0.46 | -1.99 |
| 10-14 14:32 | +20 | HYPE | DOWN | 0.62 | 0.86 | 2.10 |
| 10-14 14:32 | +15 | HYPE | DOWN | 0.62 | 0.79 | 1.37 |
| 10-14 14:32 | +10 | HYPE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-14 14:32 | +5 | HYPE | DOWN | 0.65 | 0.76 | 0.79 |
| 10-14 14:31 | +10 stop | NEAR | DOWN | 0.55 | 0.65 | 0.66 |
| 10-14 14:31 | +20 | NEAR | DOWN | 0.55 | 0.81 | 2.31 |
| 10-14 14:31 | +15 | NEAR | DOWN | 0.55 | 0.81 | 2.31 |
| 10-14 14:31 | +10 | NEAR | DOWN | 0.55 | 0.65 | 0.66 |
| 10-14 14:31 | +5 | NEAR | DOWN | 0.55 | 0.61 | 0.25 |
| 10-14 14:31 | +10 stop | BNB | DOWN | 0.56 | 0.68 | 0.86 |
| 10-14 14:31 | +20 | BNB | DOWN | 0.56 | 0.82 | 2.31 |
| 10-14 14:31 | +15 | BNB | DOWN | 0.56 | 0.71 | 1.17 |
| 10-14 14:31 | +10 | BNB | DOWN | 0.56 | 0.68 | 0.86 |
| 10-14 14:31 | +5 | BNB | DOWN | 0.56 | 0.61 | 0.15 |
| 10-14 14:31 | +10 stop | ETH | DOWN | 0.55 | 0.38 | -2.05 |
| 10-14 14:31 | +20 | ETH | DOWN | 0.55 | 0.76 | 1.79 |
| 10-14 14:31 | +15 | ETH | DOWN | 0.55 | 0.71 | 1.27 |
| 10-14 14:31 | +10 | ETH | DOWN | 0.55 | 0.68 | 0.96 |
| 10-14 14:31 | +5 | ETH | DOWN | 0.55 | 0.61 | 0.25 |
| 10-14 14:31 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
