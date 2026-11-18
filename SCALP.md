# Range-Scalp Bot

*Updated Wed Nov 18 15:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64112 | 55907 | 8205 (124) | 8 | $-17552.38 | -4.3% |
| **+10¢** | 47885 | 38283 | 9602 (165) | 8 | $-16474.31 | -5.5% |
| **+15¢** | 40148 | 29799 | 10349 (210) | 8 | $-14928.62 | -5.9% |
| **+20¢** | 35752 | 24890 | 10862 (265) | 8 | $-13225.66 | -5.9% |
| **+10¢ (15¢ stop)** | 78007 | 77843 | 164 (98) | 3 | $-28690.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 15:22 | +15 | ZEC | UP | 0.70 | open |  |
| 11-18 15:22 | +5 | ZEC | UP | 0.70 | open |  |
| 11-18 15:22 | +10 stop | ZEC | UP | 0.71 | open |  |
| 11-18 15:22 | +10 | ZEC | UP | 0.71 | open |  |
| 11-18 15:22 | +10 stop | BNB | DOWN | 0.52 | 0.67 | 1.16 |
| 11-18 15:22 | +10 stop | HYPE | DOWN | 0.59 | open |  |
| 11-18 15:22 | +10 stop | BTC | DOWN | 0.67 | 0.52 | -1.84 |
| 11-18 15:22 | +10 stop | ETH | DOWN | 0.66 | open |  |
| 11-18 15:21 | +10 | SOL | UP | 0.64 | open |  |
| 11-18 15:21 | +10 stop | BTC | UP | 0.61 | 0.42 | -2.25 |
| 11-18 15:21 | +10 stop | BNB | UP | 0.68 | 0.48 | -2.34 |
| 11-18 15:21 | +5 | BNB | UP | 0.68 | open |  |
| 11-18 15:21 | +10 stop | ETH | UP | 0.66 | 0.42 | -2.74 |
| 11-18 15:21 | +10 stop | DOGE | UP | 0.59 | 0.43 | -1.95 |
| 11-18 15:20 | +10 stop | NEAR | UP | 0.69 | 0.51 | -2.12 |
| 11-18 15:20 | +5 | BTC | UP | 0.69 | open |  |
| 11-18 15:20 | +10 stop | HYPE | UP | 0.70 | 0.52 | -2.11 |
| 11-18 15:20 | +10 stop | SOL | UP | 0.68 | 0.51 | -2.02 |
| 11-18 15:20 | +5 | SOL | UP | 0.68 | open |  |
| 11-18 15:20 | +10 stop | ZEC | UP | 0.62 | 0.74 | 0.89 |
| 11-18 15:19 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 11-18 15:19 | +10 stop | NEAR | DOWN | 0.59 | 0.41 | -2.14 |
| 11-18 15:19 | +10 stop | XRP | DOWN | 0.57 | 0.72 | 1.17 |
| 11-18 15:19 | +15 | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 11-18 15:19 | +10 | XRP | DOWN | 0.58 | 0.72 | 1.07 |
| 11-18 15:19 | +5 | XRP | DOWN | 0.58 | 0.65 | 0.36 |
| 11-18 15:19 | +10 stop | HYPE | DOWN | 0.51 | 0.63 | 0.85 |
| 11-18 15:18 | +10 stop | BTC | DOWN | 0.50 | 0.34 | -1.94 |
| 11-18 15:18 | +5 | BTC | DOWN | 0.50 | 0.56 | 0.24 |
| 11-18 15:18 | +5 | SOL | DOWN | 0.48 | 0.55 | 0.34 |
| 11-18 15:18 | +10 stop | ETH | DOWN | 0.68 | 0.50 | -2.14 |
| 11-18 15:18 | +5 | ETH | DOWN | 0.67 | open |  |
| 11-18 15:17 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-18 15:17 | +10 stop | ZEC | DOWN | 0.60 | 0.45 | -1.85 |
| 11-18 15:17 | +10 stop | SOL | DOWN | 0.58 | 0.42 | -1.96 |
| 11-18 15:17 | +10 stop | BNB | DOWN | 0.59 | 0.37 | -2.54 |
| 11-18 15:17 | +5 | SOL | DOWN | 0.58 | 0.65 | 0.36 |
| 11-18 15:17 | +10 stop | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-18 15:17 | +10 stop | NEAR | DOWN | 0.66 | 0.80 | 1.12 |
| 11-18 15:17 | +5 | BTC | DOWN | 0.55 | 0.61 | 0.25 |
