# Range-Scalp Bot

*Updated Sun Nov 08 00:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51723 | 45102 | 6621 (80) | 5 | $-14330.53 | -4.4% |
| **+10¢** | 38597 | 30877 | 7720 (106) | 5 | $-13330.77 | -5.5% |
| **+15¢** | 32320 | 24000 | 8320 (135) | 6 | $-12227.56 | -6.0% |
| **+20¢** | 28749 | 20026 | 8723 (180) | 7 | $-10775.20 | -6.0% |
| **+10¢ (15¢ stop)** | 62979 | 62876 | 103 (61) | 2 | $-23318.35 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 00:25 | +10 stop | BTC | DOWN | 0.61 | open |  |
| 11-08 00:24 | +10 stop | ETH | UP | 0.67 | 0.38 | -3.23 |
| 11-08 00:23 | +10 stop | XRP | UP | 0.68 | 0.37 | -3.43 |
| 11-08 00:23 | +10 stop | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 11-08 00:23 | +20 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 11-08 00:23 | +15 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 11-08 00:23 | +10 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 11-08 00:23 | +5 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 11-08 00:22 | +10 stop | BNB | UP | 0.60 | open |  |
| 11-08 00:22 | +10 stop | BTC | UP | 0.62 | 0.40 | -2.54 |
| 11-08 00:22 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.74 |
| 11-08 00:22 | +20 | NEAR | DOWN | 0.65 | open |  |
| 11-08 00:22 | +15 | NEAR | DOWN | 0.65 | 0.82 | 1.47 |
| 11-08 00:22 | +10 | NEAR | DOWN | 0.65 | 0.75 | 0.74 |
| 11-08 00:22 | +5 | NEAR | DOWN | 0.65 | 0.72 | 0.43 |
| 11-08 00:21 | +5 | XRP | DOWN | 0.71 | open |  |
| 11-08 00:21 | +10 stop | ETH | DOWN | 0.56 | 0.33 | -2.64 |
| 11-08 00:20 | +5 | BNB | DOWN | 0.63 | open |  |
| 11-08 00:20 | +10 stop | DOGE | DOWN | 0.49 | 0.61 | 0.85 |
| 11-08 00:20 | +20 | DOGE | DOWN | 0.47 | open |  |
| 11-08 00:20 | +15 | DOGE | DOWN | 0.47 | open |  |
| 11-08 00:20 | +10 | DOGE | DOWN | 0.47 | 0.61 | 1.05 |
| 11-08 00:20 | +5 | DOGE | DOWN | 0.47 | 0.61 | 1.05 |
| 11-08 00:19 | +5 | HYPE | DOWN | 0.70 | open |  |
| 11-08 00:19 | +10 stop | HYPE | DOWN | 0.69 | 0.50 | -2.23 |
| 11-08 00:19 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 11-08 00:19 | +10 stop | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 11-08 00:19 | +10 stop | BTC | DOWN | 0.63 | 0.32 | -3.43 |
| 11-08 00:19 | +20 | BTC | DOWN | 0.63 | open |  |
| 11-08 00:19 | +15 | BTC | DOWN | 0.63 | open |  |
| 11-08 00:19 | +10 | BTC | DOWN | 0.63 | open |  |
| 11-08 00:19 | +5 | BTC | DOWN | 0.63 | open |  |
| 11-08 00:19 | +10 stop | ETH | DOWN | 0.70 | 0.54 | -1.93 |
| 11-08 00:19 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-08 00:19 | +15 | ETH | DOWN | 0.68 | open |  |
| 11-08 00:19 | +10 | ETH | DOWN | 0.69 | open |  |
| 11-08 00:19 | +5 | ETH | DOWN | 0.69 | open |  |
| 11-08 00:18 | +10 stop | SOL | DOWN | 0.53 | 0.67 | 1.06 |
| 11-08 00:18 | +20 | SOL | DOWN | 0.53 | 0.75 | 1.88 |
| 11-08 00:18 | +15 | SOL | DOWN | 0.54 | 0.75 | 1.78 |
