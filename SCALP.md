# Range-Scalp Bot

*Updated Thu Nov 19 01:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64534 | 56293 | 8241 (124) | 0 | $-17560.98 | -4.3% |
| **+10¢** | 48213 | 38576 | 9637 (165) | 0 | $-16362.92 | -5.4% |
| **+15¢** | 40432 | 30045 | 10387 (210) | 0 | $-14765.91 | -5.8% |
| **+20¢** | 36007 | 25103 | 10904 (265) | 0 | $-13049.70 | -5.8% |
| **+10¢ (15¢ stop)** | 78544 | 78380 | 164 (98) | 0 | $-28891.30 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 01:16 | +10 stop | HYPE | DOWN | 0.63 | 0.77 | 1.10 |
| 11-19 01:16 | +20 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-19 01:16 | +15 | HYPE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-19 01:16 | +10 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-19 01:16 | +5 | HYPE | DOWN | 0.63 | 0.68 | 0.17 |
| 11-19 01:12 | +10 stop | HYPE | DOWN | 0.68 | 0.27 | -4.36 |
| 11-19 01:12 | +10 stop | ETH | UP | 0.59 | 0.80 | 1.81 |
| 11-19 01:12 | +10 stop | BNB | UP | 0.71 | 0.48 | -2.63 |
| 11-19 01:11 | +10 stop | BNB | UP | 0.67 | 0.79 | 0.97 |
| 11-19 01:11 | +20 | BNB | UP | 0.67 | 0.95 | 2.63 |
| 11-19 01:11 | +15 | BNB | UP | 0.67 | 0.95 | 2.63 |
| 11-19 01:11 | +10 stop | HYPE | UP | 0.68 | 0.52 | -1.94 |
| 11-19 01:10 | +10 stop | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-19 01:10 | +15 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-19 01:10 | +10 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-19 01:10 | +5 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-19 01:10 | +10 stop | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-19 01:09 | +10 stop | ETH | UP | 0.59 | 0.74 | 1.19 |
| 11-19 01:09 | +10 stop | BNB | DOWN | 0.48 | 0.23 | -2.81 |
| 11-19 01:09 | +10 | BNB | DOWN | 0.50 | yes | -5.18 |
| 11-19 01:09 | +5 | BNB | DOWN | 0.51 | yes | -5.28 |
| 11-19 01:09 | +10 stop | XRP | DOWN | 0.55 | 0.26 | -3.22 |
| 11-19 01:08 | +10 stop | ETH | UP | 0.65 | 0.50 | -1.84 |
| 11-19 01:08 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-19 01:08 | +10 stop | BNB | UP | 0.47 | 0.59 | 0.85 |
| 11-19 01:08 | +20 | BNB | UP | 0.47 | 0.74 | 2.38 |
| 11-19 01:08 | +15 | BNB | UP | 0.47 | 0.74 | 2.38 |
| 11-19 01:08 | +10 | BNB | UP | 0.47 | 0.59 | 0.85 |
| 11-19 01:08 | +5 | BNB | UP | 0.48 | 0.59 | 0.73 |
| 11-19 01:08 | +10 stop | XRP | UP | 0.44 | 0.63 | 1.55 |
| 11-19 01:08 | +10 stop | HYPE | UP | 0.42 | 0.53 | 0.74 |
| 11-19 01:08 | +10 stop | DOGE | UP | 0.46 | 0.67 | 1.76 |
| 11-19 01:08 | +10 stop | BTC | UP | 0.49 | 0.69 | 1.67 |
| 11-19 01:07 | +10 stop | NEAR | DOWN | 0.57 | 0.75 | 1.48 |
| 11-19 01:07 | +10 stop | ZEC | DOWN | 0.47 | 0.60 | 0.95 |
| 11-19 01:06 | +10 stop | HYPE | UP | 0.62 | 0.73 | 0.79 |
| 11-19 01:06 | +10 stop | BNB | UP | 0.63 | 0.84 | 1.84 |
| 11-19 01:06 | +10 | BNB | UP | 0.62 | 0.84 | 1.93 |
| 11-19 01:06 | +5 | BNB | UP | 0.62 | 0.68 | 0.27 |
| 11-19 01:06 | +10 stop | SOL | UP | 0.63 | 0.76 | 1.00 |
