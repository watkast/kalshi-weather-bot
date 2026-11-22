# Range-Scalp Bot

*Updated Sun Nov 22 13:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68715 | 59961 | 8754 (142) | 0 | $-18485.96 | -4.3% |
| **+10¢** | 51288 | 41066 | 10222 (186) | 3 | $-17127.41 | -5.3% |
| **+15¢** | 42978 | 31959 | 11019 (237) | 5 | $-15374.62 | -5.7% |
| **+20¢** | 38260 | 26682 | 11578 (295) | 5 | $-13692.75 | -5.7% |
| **+10¢ (15¢ stop)** | 83676 | 83491 | 185 (116) | 0 | $-30802.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 13:12 | +10 stop | NEAR | UP | 0.58 | 0.76 | 1.49 |
| 11-22 13:12 | +10 | NEAR | UP | 0.59 | 0.76 | 1.40 |
| 11-22 13:12 | +5 | NEAR | UP | 0.58 | 0.63 | 0.15 |
| 11-22 13:10 | +10 stop | NEAR | UP | 0.54 | 0.69 | 1.16 |
| 11-22 13:10 | +10 | NEAR | UP | 0.54 | 0.69 | 1.17 |
| 11-22 13:08 | +5 | XRP | DOWN | 0.63 | 0.70 | 0.38 |
| 11-22 13:08 | +5 | HYPE | DOWN | 0.60 | 0.78 | 1.48 |
| 11-22 13:07 | +10 stop | BNB | DOWN | 0.61 | 0.77 | 1.30 |
| 11-22 13:07 | +5 | BNB | DOWN | 0.61 | 0.77 | 1.30 |
| 11-22 13:06 | +10 stop | NEAR | UP | 0.64 | 0.46 | -2.15 |
| 11-22 13:06 | +5 | NEAR | UP | 0.64 | 0.69 | 0.18 |
| 11-22 13:06 | +10 stop | ZEC | UP | 0.65 | 0.76 | 0.81 |
| 11-22 13:06 | +10 stop | NEAR | DOWN | 0.43 | 0.56 | 0.94 |
| 11-22 13:06 | +5 | NEAR | DOWN | 0.44 | 0.56 | 0.84 |
| 11-22 13:05 | +10 stop | XRP | DOWN | 0.70 | 0.86 | 1.36 |
| 11-22 13:05 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 11-22 13:05 | +10 stop | HYPE | DOWN | 0.70 | 0.53 | -2.07 |
| 11-22 13:04 | +5 | HYPE | DOWN | 0.70 | 0.77 | 0.42 |
| 11-22 13:04 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-22 13:04 | +10 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-22 13:04 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 11-22 13:04 | +5 | XRP | DOWN | 0.61 | 0.66 | 0.17 |
| 11-22 13:04 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-22 13:04 | +10 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-22 13:04 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 11-22 13:03 | +10 stop | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 11-22 13:03 | +5 | XRP | DOWN | 0.55 | 0.62 | 0.35 |
| 11-22 13:03 | +5 | SOL | DOWN | 0.43 | 0.54 | 0.74 |
| 11-22 13:03 | +5 | HYPE | DOWN | 0.45 | 0.52 | 0.34 |
| 11-22 13:03 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-22 13:03 | +5 | BTC | DOWN | 0.65 | 0.73 | 0.50 |
| 11-22 13:03 | +5 | BNB | DOWN | 0.64 | 0.72 | 0.48 |
| 11-22 13:03 | +10 stop | NEAR | UP | 0.55 | 0.32 | -2.62 |
| 11-22 13:03 | +10 stop | HYPE | UP | 0.49 | 0.31 | -2.13 |
| 11-22 13:03 | +5 | HYPE | UP | 0.49 | 0.57 | 0.44 |
| 11-22 13:02 | +10 stop | ZEC | UP | 0.58 | 0.43 | -1.86 |
| 11-22 13:02 | +5 | ETH | DOWN | 0.61 | 0.70 | 0.58 |
| 11-22 13:02 | +5 | BTC | DOWN | 0.58 | 0.64 | 0.25 |
| 11-22 13:02 | +10 stop | DOGE | DOWN | 0.60 | 0.71 | 0.77 |
| 11-22 13:02 | +20 | DOGE | DOWN | 0.60 | 0.81 | 1.82 |
