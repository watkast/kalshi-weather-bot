# Range-Scalp Bot

*Updated Sat Nov 28 08:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74394 | 64935 | 9459 (171) | 0 | $-19746.50 | -4.2% |
| **+10¢** | 55425 | 44371 | 11054 (217) | 0 | $-18384.05 | -5.3% |
| **+15¢** | 46407 | 34504 | 11903 (275) | 1 | $-16430.47 | -5.6% |
| **+20¢** | 41296 | 28763 | 12533 (342) | 2 | $-14823.51 | -5.7% |
| **+10¢ (15¢ stop)** | 90533 | 90313 | 220 (136) | 0 | $-33417.25 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 08:38 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-28 08:38 | +20 | SOL | DOWN | 0.67 | 0.88 | 1.86 |
| 11-28 08:38 | +15 | SOL | DOWN | 0.67 | 0.84 | 1.44 |
| 11-28 08:38 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-28 08:38 | +5 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-28 08:32 | +5 | BNB | DOWN | 0.61 | 0.79 | 1.50 |
| 11-28 08:32 | +10 stop | BTC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-28 08:32 | +20 | BTC | DOWN | 0.63 | 0.85 | 1.94 |
| 11-28 08:32 | +15 | BTC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-28 08:32 | +10 | BTC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-28 08:32 | +5 | BTC | DOWN | 0.63 | 0.70 | 0.38 |
| 11-28 08:32 | +10 stop | HYPE | DOWN | 0.51 | 0.71 | 1.67 |
| 11-28 08:32 | +10 | HYPE | DOWN | 0.51 | 0.71 | 1.67 |
| 11-28 08:32 | +5 | HYPE | DOWN | 0.51 | 0.71 | 1.67 |
| 11-28 08:31 | +10 stop | NEAR | DOWN | 0.61 | 0.45 | -1.95 |
| 11-28 08:31 | +15 | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 11-28 08:31 | +10 | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 11-28 08:31 | +5 | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 11-28 08:31 | +10 stop | BNB | DOWN | 0.66 | 0.79 | 1.03 |
| 11-28 08:31 | +20 | BNB | DOWN | 0.66 | 0.88 | 1.97 |
| 11-28 08:31 | +15 | BNB | DOWN | 0.66 | 0.83 | 1.45 |
| 11-28 08:31 | +10 | BNB | DOWN | 0.66 | 0.79 | 1.03 |
| 11-28 08:31 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.20 |
| 11-28 08:31 | +10 stop | ZEC | DOWN | 0.56 | 0.66 | 0.69 |
| 11-28 08:31 | +20 | ZEC | DOWN | 0.54 | 0.85 | 2.80 |
| 11-28 08:31 | +15 | ZEC | DOWN | 0.54 | 0.85 | 2.80 |
| 11-28 08:31 | +10 | ZEC | DOWN | 0.54 | 0.66 | 0.83 |
| 11-28 08:31 | +5 | ZEC | DOWN | 0.54 | 0.66 | 0.83 |
| 11-28 08:31 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-28 08:31 | +20 | SOL | DOWN | 0.64 | 0.85 | 1.84 |
| 11-28 08:31 | +15 | SOL | DOWN | 0.64 | 0.82 | 1.52 |
| 11-28 08:31 | +10 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-28 08:31 | +5 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-28 08:31 | +10 stop | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-28 08:31 | +20 | ETH | DOWN | 0.68 | 0.91 | 2.02 |
| 11-28 08:31 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-28 08:31 | +10 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-28 08:31 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 11-28 08:31 | +10 stop | BNB | UP | 0.39 | 0.60 | 1.76 |
| 11-28 08:31 | +20 | BNB | UP | 0.39 | 0.60 | 1.76 |
