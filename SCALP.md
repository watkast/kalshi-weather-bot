# Range-Scalp Bot

*Updated Fri Oct 09 01:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8313 | 7193 | 1120 (13) | 3 | $-2697.30 | -5.1% |
| **+10¢** | 6302 | 4978 | 1324 (25) | 3 | $-2649.60 | -6.7% |
| **+15¢** | 5315 | 3921 | 1394 (37) | 3 | $-2146.18 | -6.4% |
| **+20¢** | 4735 | 3289 | 1446 (45) | 4 | $-1746.36 | -5.9% |
| **+10¢ (15¢ stop)** | 10103 | 10073 | 30 (19) | 3 | $-3738.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 01:38 | +10 | BTC | DOWN | 0.61 | open |  |
| 10-09 01:38 | +5 | BTC | DOWN | 0.61 | open |  |
| 10-09 01:38 | +10 stop | XRP | UP | 0.54 | open |  |
| 10-09 01:38 | +10 stop | BTC | DOWN | 0.56 | open |  |
| 10-09 01:38 | +15 | BTC | DOWN | 0.55 | open |  |
| 10-09 01:38 | +10 | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 10-09 01:38 | +5 | BTC | DOWN | 0.57 | 0.65 | 0.46 |
| 10-09 01:38 | +10 stop | DOGE | DOWN | 0.58 | open |  |
| 10-09 01:38 | +10 | DOGE | DOWN | 0.58 | open |  |
| 10-09 01:38 | +5 | DOGE | DOWN | 0.58 | open |  |
| 10-09 01:37 | +10 stop | XRP | DOWN | 0.67 | 0.41 | -2.93 |
| 10-09 01:35 | +10 stop | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-09 01:35 | +20 | DOGE | DOWN | 0.61 | open |  |
| 10-09 01:35 | +15 | DOGE | DOWN | 0.61 | open |  |
| 10-09 01:35 | +10 | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-09 01:35 | +5 | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-09 01:35 | +5 | ETH | DOWN | 0.66 | 0.74 | 0.50 |
| 10-09 01:35 | +10 stop | XRP | UP | 0.62 | 0.42 | -2.35 |
| 10-09 01:35 | +20 | XRP | UP | 0.62 | open |  |
| 10-09 01:35 | +15 | XRP | UP | 0.62 | open |  |
| 10-09 01:35 | +10 | XRP | UP | 0.62 | open |  |
| 10-09 01:35 | +5 | XRP | UP | 0.62 | open |  |
| 10-09 01:35 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-09 01:35 | +15 | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 10-09 01:35 | +10 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-09 01:35 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-09 01:34 | +10 stop | HYPE | DOWN | 0.56 | 0.71 | 1.13 |
| 10-09 01:34 | +20 | HYPE | DOWN | 0.56 | 0.78 | 1.89 |
| 10-09 01:34 | +15 | HYPE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-09 01:34 | +10 | HYPE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-09 01:34 | +5 | HYPE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-09 01:34 | +10 stop | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 10-09 01:34 | +20 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 10-09 01:34 | +15 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 10-09 01:34 | +10 | ETH | DOWN | 0.59 | 0.74 | 1.19 |
| 10-09 01:34 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 10-09 01:34 | +10 stop | SOL | DOWN | 0.58 | 0.71 | 0.97 |
| 10-09 01:34 | +20 | SOL | DOWN | 0.58 | 0.81 | 2.01 |
| 10-09 01:34 | +15 | SOL | DOWN | 0.58 | 0.73 | 1.18 |
| 10-09 01:34 | +10 | SOL | DOWN | 0.58 | 0.71 | 0.97 |
