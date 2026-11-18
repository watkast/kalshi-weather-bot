# Range-Scalp Bot

*Updated Wed Nov 18 14:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64025 | 55839 | 8186 (124) | 3 | $-17465.03 | -4.3% |
| **+10¢** | 47826 | 38248 | 9578 (165) | 5 | $-16357.36 | -5.4% |
| **+15¢** | 40101 | 29776 | 10325 (210) | 4 | $-14808.91 | -5.9% |
| **+20¢** | 35713 | 24874 | 10839 (265) | 3 | $-13112.16 | -5.9% |
| **+10¢ (15¢ stop)** | 77877 | 77713 | 164 (98) | 0 | $-28569.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 14:11 | +15 | ZEC | UP | 0.67 | open |  |
| 11-18 14:11 | +10 | ZEC | UP | 0.66 | open |  |
| 11-18 14:11 | +5 | ZEC | UP | 0.66 | open |  |
| 11-18 14:10 | +10 stop | ETH | UP | 0.55 | 0.77 | 1.89 |
| 11-18 14:10 | +20 | ETH | UP | 0.54 | 0.77 | 1.99 |
| 11-18 14:10 | +15 | ETH | UP | 0.54 | 0.77 | 1.99 |
| 11-18 14:10 | +10 | ETH | UP | 0.55 | 0.77 | 1.89 |
| 11-18 14:10 | +5 | ETH | UP | 0.55 | 0.77 | 1.89 |
| 11-18 14:10 | +5 | BNB | UP | 0.59 | 0.76 | 1.40 |
| 11-18 14:10 | +10 stop | BTC | DOWN | 0.66 | 0.40 | -2.93 |
| 11-18 14:10 | +20 | BTC | DOWN | 0.66 | open |  |
| 11-18 14:10 | +15 | BTC | DOWN | 0.66 | open |  |
| 11-18 14:10 | +10 | BTC | DOWN | 0.66 | open |  |
| 11-18 14:10 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-18 14:10 | +10 stop | SOL | UP | 0.70 | 0.82 | 0.94 |
| 11-18 14:10 | +20 | SOL | UP | 0.71 | 0.92 | 1.94 |
| 11-18 14:10 | +15 | SOL | UP | 0.71 | 0.92 | 1.94 |
| 11-18 14:10 | +10 | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-18 14:10 | +5 | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-18 14:10 | +10 stop | BNB | UP | 0.58 | 0.76 | 1.48 |
| 11-18 14:10 | +20 | BNB | UP | 0.58 | 0.91 | 3.04 |
| 11-18 14:10 | +15 | BNB | UP | 0.56 | 0.76 | 1.66 |
| 11-18 14:10 | +10 | BNB | UP | 0.52 | 0.76 | 2.06 |
| 11-18 14:10 | +5 | BNB | UP | 0.52 | 0.62 | 0.62 |
| 11-18 14:08 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-18 14:08 | +5 | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-18 14:07 | +10 stop | BNB | UP | 0.68 | 0.82 | 1.13 |
| 11-18 14:07 | +10 | BNB | UP | 0.68 | 0.82 | 1.13 |
| 11-18 14:07 | +5 | BNB | UP | 0.68 | 0.82 | 1.13 |
| 11-18 14:06 | +5 | ZEC | UP | 0.71 | 0.79 | 0.56 |
| 11-18 14:06 | +10 stop | NEAR | DOWN | 0.50 | 0.70 | 1.67 |
| 11-18 14:06 | +20 | NEAR | DOWN | 0.50 | 0.70 | 1.67 |
| 11-18 14:06 | +10 stop | HYPE | DOWN | 0.58 | 0.74 | 1.28 |
| 11-18 14:06 | +5 | HYPE | DOWN | 0.59 | 0.74 | 1.19 |
| 11-18 14:06 | +10 stop | ZEC | UP | 0.61 | 0.79 | 1.51 |
| 11-18 14:06 | +10 | ZEC | UP | 0.61 | 0.79 | 1.51 |
| 11-18 14:06 | +5 | ZEC | UP | 0.61 | 0.67 | 0.27 |
| 11-18 14:05 | +10 stop | BTC | UP | 0.58 | 0.74 | 1.28 |
| 11-18 14:05 | +10 | BTC | UP | 0.58 | 0.74 | 1.28 |
| 11-18 14:05 | +10 stop | HYPE | UP | 0.50 | 0.63 | 0.95 |
