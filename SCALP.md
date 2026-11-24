# Range-Scalp Bot

*Updated Tue Nov 24 08:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70672 | 61686 | 8986 (148) | 0 | $-18898.33 | -4.2% |
| **+10¢** | 52716 | 42224 | 10492 (193) | 0 | $-17488.40 | -5.3% |
| **+15¢** | 44165 | 32866 | 11299 (250) | 0 | $-15538.71 | -5.6% |
| **+20¢** | 39331 | 27435 | 11896 (316) | 0 | $-13899.84 | -5.6% |
| **+10¢ (15¢ stop)** | 86047 | 85849 | 198 (118) | 0 | $-31640.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 08:10 | +20 | XRP | DOWN | 0.69 | 0.92 | 2.10 |
| 11-24 08:10 | +15 | XRP | DOWN | 0.69 | 0.85 | 1.33 |
| 11-24 08:10 | +10 | XRP | DOWN | 0.69 | 0.85 | 1.36 |
| 11-24 08:10 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 11-24 08:10 | +10 stop | NEAR | DOWN | 0.62 | 0.78 | 1.30 |
| 11-24 08:10 | +10 stop | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 11-24 08:10 | +20 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 11-24 08:10 | +15 | SOL | DOWN | 0.70 | 0.89 | 1.68 |
| 11-24 08:10 | +10 | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-24 08:10 | +5 | SOL | DOWN | 0.69 | 0.82 | 1.04 |
| 11-24 08:06 | +10 stop | HYPE | UP | 0.58 | 0.33 | -2.84 |
| 11-24 08:06 | +20 | HYPE | UP | 0.58 | no | -5.98 |
| 11-24 08:06 | +15 | HYPE | UP | 0.58 | no | -5.98 |
| 11-24 08:06 | +10 | HYPE | UP | 0.58 | no | -5.98 |
| 11-24 08:06 | +5 | HYPE | UP | 0.58 | 0.64 | 0.25 |
| 11-24 08:05 | +10 stop | SOL | DOWN | 0.62 | 0.86 | 2.14 |
| 11-24 08:05 | +10 | SOL | DOWN | 0.62 | 0.86 | 2.14 |
| 11-24 08:05 | +5 | SOL | DOWN | 0.62 | 0.71 | 0.58 |
| 11-24 08:05 | +10 stop | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 11-24 08:05 | +10 stop | ETH | DOWN | 0.64 | 0.81 | 1.42 |
| 11-24 08:05 | +10 | ETH | DOWN | 0.63 | 0.81 | 1.52 |
| 11-24 08:05 | +5 | ETH | DOWN | 0.64 | 0.81 | 1.42 |
| 11-24 08:04 | +10 stop | ZEC | DOWN | 0.66 | 0.85 | 1.65 |
| 11-24 08:04 | +15 | ZEC | DOWN | 0.66 | 0.85 | 1.65 |
| 11-24 08:04 | +10 | ZEC | DOWN | 0.66 | 0.85 | 1.65 |
| 11-24 08:04 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-24 08:04 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-24 08:04 | +10 | BNB | DOWN | 0.70 | 0.84 | 1.15 |
| 11-24 08:04 | +5 | BNB | DOWN | 0.70 | 0.77 | 0.42 |
| 11-24 08:04 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 11-24 08:04 | +5 | SOL | DOWN | 0.63 | 0.70 | 0.38 |
| 11-24 08:03 | +5 | BTC | DOWN | 0.58 | 0.73 | 1.18 |
| 11-24 08:03 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.28 |
| 11-24 08:03 | +10 stop | XRP | DOWN | 0.56 | 0.69 | 0.97 |
| 11-24 08:03 | +10 stop | BNB | DOWN | 0.56 | 0.68 | 0.85 |
| 11-24 08:03 | +20 | BNB | DOWN | 0.56 | 0.77 | 1.78 |
| 11-24 08:03 | +15 | BNB | DOWN | 0.56 | 0.77 | 1.78 |
| 11-24 08:03 | +10 | BNB | DOWN | 0.56 | 0.66 | 0.66 |
| 11-24 08:03 | +5 | BNB | DOWN | 0.56 | 0.62 | 0.25 |
| 11-24 08:03 | +10 stop | ZEC | DOWN | 0.50 | 0.67 | 1.36 |
