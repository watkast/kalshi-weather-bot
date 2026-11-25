# Range-Scalp Bot

*Updated Wed Nov 25 20:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72068 | 62907 | 9161 (158) | 0 | $-19153.43 | -4.2% |
| **+10¢** | 53766 | 43066 | 10700 (203) | 0 | $-17758.39 | -5.3% |
| **+15¢** | 45018 | 33494 | 11524 (260) | 0 | $-15840.54 | -5.6% |
| **+20¢** | 40081 | 27944 | 12137 (326) | 0 | $-14230.10 | -5.7% |
| **+10¢ (15¢ stop)** | 87729 | 87520 | 209 (128) | 0 | $-32155.36 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 20:28 | +10 stop | SOL | DOWN | 0.64 | 0.82 | 1.52 |
| 11-25 20:28 | +20 | SOL | DOWN | 0.65 | 0.96 | 2.97 |
| 11-25 20:28 | +15 | SOL | DOWN | 0.65 | 0.82 | 1.44 |
| 11-25 20:28 | +10 | SOL | DOWN | 0.66 | 0.82 | 1.35 |
| 11-25 20:28 | +5 | SOL | DOWN | 0.65 | 0.82 | 1.44 |
| 11-25 20:28 | +10 stop | XRP | UP | 0.69 | 0.98 | 2.76 |
| 11-25 20:28 | +5 | XRP | UP | 0.71 | 0.98 | 2.58 |
| 11-25 20:27 | +10 stop | SOL | UP | 0.41 | 0.65 | 2.08 |
| 11-25 20:27 | +20 | SOL | UP | 0.41 | 0.65 | 2.07 |
| 11-25 20:27 | +15 | SOL | UP | 0.43 | 0.65 | 1.89 |
| 11-25 20:27 | +10 | SOL | UP | 0.43 | 0.65 | 1.89 |
| 11-25 20:27 | +5 | SOL | UP | 0.43 | 0.65 | 1.88 |
| 11-25 20:27 | +10 stop | ZEC | UP | 0.54 | 0.36 | -2.15 |
| 11-25 20:27 | +20 | ZEC | UP | 0.54 | no | -5.58 |
| 11-25 20:27 | +15 | ZEC | UP | 0.54 | no | -5.58 |
| 11-25 20:27 | +10 | ZEC | UP | 0.55 | no | -5.66 |
| 11-25 20:27 | +5 | ZEC | UP | 0.54 | no | -5.62 |
| 11-25 20:27 | +10 stop | ETH | UP | 0.63 | 0.24 | -4.20 |
| 11-25 20:27 | +10 stop | BNB | UP | 0.65 | 0.45 | -2.34 |
| 11-25 20:26 | +10 stop | ETH | DOWN | 0.37 | 0.55 | 1.45 |
| 11-25 20:25 | +10 stop | BTC | DOWN | 0.58 | 0.79 | 1.80 |
| 11-25 20:25 | +10 stop | BNB | UP | 0.69 | 0.45 | -2.78 |
| 11-25 20:25 | +15 | BNB | UP | 0.69 | no | -7.10 |
| 11-25 20:25 | +10 | BNB | UP | 0.69 | no | -7.05 |
| 11-25 20:25 | +5 | BNB | UP | 0.68 | no | -6.96 |
| 11-25 20:24 | +10 stop | BTC | UP | 0.44 | 0.54 | 0.64 |
| 11-25 20:23 | +10 stop | BTC | UP | 0.49 | 0.61 | 0.85 |
| 11-25 20:23 | +10 stop | ETH | UP | 0.70 | 0.42 | -3.13 |
| 11-25 20:22 | +5 | HYPE | UP | 0.71 | 0.84 | 1.05 |
| 11-25 20:22 | +10 stop | BNB | UP | 0.63 | 0.73 | 0.69 |
| 11-25 20:22 | +10 stop | ZEC | UP | 0.63 | 0.76 | 1.00 |
| 11-25 20:22 | +5 | ZEC | UP | 0.63 | 0.76 | 1.00 |
| 11-25 20:22 | +10 stop | BTC | DOWN | 0.47 | 0.61 | 1.05 |
| 11-25 20:21 | +10 stop | ETH | DOWN | 0.63 | 0.42 | -2.45 |
| 11-25 20:21 | +5 | ETH | DOWN | 0.63 | 0.75 | 0.89 |
| 11-25 20:21 | +10 stop | SOL | UP | 0.65 | 0.75 | 0.70 |
| 11-25 20:21 | +10 | SOL | UP | 0.65 | 0.75 | 0.70 |
| 11-25 20:21 | +5 | SOL | UP | 0.65 | 0.75 | 0.70 |
| 11-25 20:21 | +10 stop | HYPE | UP | 0.61 | 0.71 | 0.68 |
| 11-25 20:21 | +10 | HYPE | UP | 0.61 | 0.71 | 0.68 |
