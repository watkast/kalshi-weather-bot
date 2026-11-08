# Range-Scalp Bot

*Updated Sun Nov 08 02:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51839 | 45205 | 6634 (80) | 1 | $-14348.11 | -4.4% |
| **+10¢** | 38685 | 30950 | 7735 (106) | 5 | $-13345.96 | -5.5% |
| **+15¢** | 32393 | 24057 | 8336 (135) | 5 | $-12233.08 | -6.0% |
| **+20¢** | 28818 | 20079 | 8739 (180) | 5 | $-10762.64 | -6.0% |
| **+10¢ (15¢ stop)** | 63134 | 63031 | 103 (61) | 0 | $-23382.42 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 02:07 | +10 stop | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 11-08 02:07 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 11-08 02:07 | +10 stop | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 11-08 02:07 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 11-08 02:07 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-08 02:07 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 11-08 02:07 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-08 02:07 | +5 | SOL | DOWN | 0.65 | 0.72 | 0.39 |
| 11-08 02:06 | +5 | DOGE | DOWN | 0.61 | 0.66 | 0.17 |
| 11-08 02:06 | +10 stop | BNB | DOWN | 0.66 | 0.87 | 1.86 |
| 11-08 02:05 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 11-08 02:05 | +10 stop | ETH | DOWN | 0.60 | 0.72 | 0.88 |
| 11-08 02:05 | +5 | ETH | DOWN | 0.61 | 0.72 | 0.82 |
| 11-08 02:05 | +5 | DOGE | DOWN | 0.59 | 0.67 | 0.47 |
| 11-08 02:04 | +10 stop | BNB | DOWN | 0.53 | 0.67 | 1.06 |
| 11-08 02:03 | +5 | BNB | UP | 0.59 | open |  |
| 11-08 02:03 | +10 stop | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 11-08 02:03 | +5 | SOL | DOWN | 0.65 | 0.80 | 1.22 |
| 11-08 02:03 | +10 stop | DOGE | DOWN | 0.67 | 0.51 | -1.94 |
| 11-08 02:03 | +20 | DOGE | DOWN | 0.67 | 0.91 | 2.16 |
| 11-08 02:03 | +15 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-08 02:03 | +10 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-08 02:03 | +5 | DOGE | DOWN | 0.67 | 0.74 | 0.40 |
| 11-08 02:02 | +5 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-08 02:02 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-08 02:02 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 11-08 02:02 | +5 | NEAR | DOWN | 0.59 | 0.64 | 0.16 |
| 11-08 02:02 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-08 02:02 | +20 | HYPE | DOWN | 0.64 | 0.87 | 2.05 |
| 11-08 02:02 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-08 02:02 | +10 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-08 02:02 | +5 | HYPE | DOWN | 0.62 | 0.70 | 0.48 |
| 11-08 02:02 | +5 | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 11-08 02:02 | +10 stop | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-08 02:02 | +20 | BTC | DOWN | 0.70 | 0.90 | 1.78 |
| 11-08 02:02 | +15 | BTC | DOWN | 0.70 | 0.85 | 1.26 |
| 11-08 02:02 | +10 | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-08 02:02 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-08 02:01 | +10 stop | XRP | UP | 0.52 | 0.36 | -1.95 |
| 11-08 02:01 | +20 | XRP | UP | 0.52 | open |  |
