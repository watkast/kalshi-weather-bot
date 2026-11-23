# Range-Scalp Bot

*Updated Mon Nov 23 01:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69342 | 60501 | 8841 (146) | 0 | $-18693.52 | -4.3% |
| **+10¢** | 51750 | 41425 | 10325 (189) | 0 | $-17355.10 | -5.3% |
| **+15¢** | 43370 | 32244 | 11126 (244) | 0 | $-15527.43 | -5.7% |
| **+20¢** | 38625 | 26929 | 11696 (305) | 0 | $-13830.25 | -5.7% |
| **+10¢ (15¢ stop)** | 84430 | 84240 | 190 (118) | 0 | $-31043.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 01:01 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-23 01:01 | +20 | BTC | DOWN | 0.71 | 0.91 | 1.79 |
| 11-23 01:01 | +15 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-23 01:01 | +10 | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-23 01:01 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 11-23 01:01 | +10 stop | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-23 01:01 | +20 | ZEC | DOWN | 0.69 | 0.91 | 1.96 |
| 11-23 01:01 | +15 | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-23 01:01 | +10 | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-23 01:01 | +5 | ZEC | DOWN | 0.69 | 0.76 | 0.42 |
| 11-23 01:01 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-23 01:01 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-23 01:01 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-23 01:01 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-23 01:01 | +5 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-23 00:59 | +10 stop | DOGE | DOWN | 0.32 | 0.55 | 1.97 |
| 11-23 00:59 | +20 | DOGE | DOWN | 0.33 | 0.55 | 1.86 |
| 11-23 00:59 | +15 | DOGE | DOWN | 0.39 | 0.55 | 1.25 |
| 11-23 00:59 | +10 | DOGE | DOWN | 0.38 | 0.55 | 1.35 |
| 11-23 00:59 | +5 | DOGE | DOWN | 0.38 | 0.55 | 1.35 |
| 11-23 00:56 | +10 stop | XRP | DOWN | 0.20 | 0.60 | 3.71 |
| 11-23 00:56 | +15 | XRP | DOWN | 0.21 | 0.60 | 3.61 |
| 11-23 00:56 | +10 | XRP | DOWN | 0.20 | 0.60 | 3.71 |
| 11-23 00:56 | +5 | XRP | DOWN | 0.20 | 0.60 | 3.71 |
| 11-23 00:55 | +10 stop | ETH | DOWN | 0.68 | 0.37 | -3.43 |
| 11-23 00:55 | +5 | ETH | DOWN | 0.67 | yes | -6.86 |
| 11-23 00:55 | +10 stop | BTC | UP | 0.66 | 0.82 | 1.33 |
| 11-23 00:54 | +10 stop | ZEC | UP | 0.58 | 0.94 | 3.41 |
| 11-23 00:54 | +15 | ZEC | UP | 0.56 | 0.94 | 3.61 |
| 11-23 00:54 | +10 stop | DOGE | DOWN | 0.58 | 0.42 | -1.96 |
| 11-23 00:53 | +15 | HYPE | UP | 0.68 | 0.92 | 2.14 |
| 11-23 00:53 | +5 | HYPE | UP | 0.68 | 0.76 | 0.51 |
| 11-23 00:53 | +10 stop | HYPE | UP | 0.70 | 0.92 | 1.95 |
| 11-23 00:53 | +20 | HYPE | UP | 0.70 | 0.92 | 1.95 |
| 11-23 00:53 | +10 stop | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 11-23 00:52 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-23 00:52 | +20 | ZEC | UP | 0.71 | 0.94 | 2.14 |
| 11-23 00:52 | +15 | ZEC | UP | 0.71 | 0.86 | 1.26 |
| 11-23 00:52 | +10 stop | BNB | UP | 0.65 | 0.80 | 1.23 |
| 11-23 00:52 | +10 stop | SOL | UP | 0.69 | 0.81 | 0.94 |
