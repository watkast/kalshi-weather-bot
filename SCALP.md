# Range-Scalp Bot

*Updated Mon Nov 23 12:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69937 | 61033 | 8904 (146) | 1 | $-18786.33 | -4.3% |
| **+10¢** | 52185 | 41781 | 10404 (189) | 1 | $-17473.60 | -5.3% |
| **+15¢** | 43733 | 32526 | 11207 (245) | 1 | $-15582.01 | -5.7% |
| **+20¢** | 38942 | 27148 | 11794 (310) | 1 | $-13942.36 | -5.7% |
| **+10¢ (15¢ stop)** | 85168 | 84978 | 190 (118) | 0 | $-31281.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 12:12 | +10 stop | HYPE | UP | 0.42 | 0.64 | 1.85 |
| 11-23 12:11 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-23 12:11 | +15 | BTC | DOWN | 0.59 | 0.78 | 1.60 |
| 11-23 12:11 | +10 | BTC | DOWN | 0.59 | 0.78 | 1.60 |
| 11-23 12:11 | +10 stop | DOGE | DOWN | 0.44 | 0.68 | 2.06 |
| 11-23 12:11 | +10 | DOGE | DOWN | 0.47 | 0.68 | 1.76 |
| 11-23 12:11 | +5 | DOGE | DOWN | 0.48 | 0.68 | 1.66 |
| 11-23 12:11 | +10 stop | HYPE | UP | 0.53 | 0.65 | 0.86 |
| 11-23 12:10 | +5 | BTC | UP | 0.56 | open |  |
| 11-23 12:10 | +10 stop | ETH | DOWN | 0.69 | 0.91 | 2.02 |
| 11-23 12:10 | +20 | ETH | DOWN | 0.69 | 0.91 | 2.02 |
| 11-23 12:10 | +15 | ETH | DOWN | 0.69 | 0.91 | 2.02 |
| 11-23 12:10 | +10 | ETH | DOWN | 0.69 | 0.91 | 2.02 |
| 11-23 12:10 | +5 | ETH | DOWN | 0.69 | 0.91 | 2.02 |
| 11-23 12:10 | +10 stop | SOL | UP | 0.66 | 0.49 | -2.04 |
| 11-23 12:09 | +10 stop | BTC | DOWN | 0.37 | 0.73 | 3.29 |
| 11-23 12:09 | +15 | BTC | DOWN | 0.37 | 0.73 | 3.29 |
| 11-23 12:09 | +10 | BTC | DOWN | 0.37 | 0.73 | 3.29 |
| 11-23 12:09 | +5 | BTC | DOWN | 0.37 | 0.46 | 0.55 |
| 11-23 12:09 | +10 stop | DOGE | UP | 0.70 | 0.28 | -4.50 |
| 11-23 12:09 | +10 stop | HYPE | DOWN | 0.45 | 0.58 | 0.93 |
| 11-23 12:09 | +10 stop | SOL | DOWN | 0.53 | 0.34 | -2.24 |
| 11-23 12:08 | +10 stop | BTC | DOWN | 0.59 | 0.78 | 1.60 |
| 11-23 12:08 | +10 | BTC | DOWN | 0.59 | 0.78 | 1.60 |
| 11-23 12:08 | +5 | BTC | DOWN | 0.59 | 0.78 | 1.60 |
| 11-23 12:07 | +10 stop | BNB | DOWN | 0.70 | 0.83 | 1.05 |
| 11-23 12:07 | +15 | BNB | DOWN | 0.70 | 0.88 | 1.57 |
| 11-23 12:07 | +10 | BNB | DOWN | 0.70 | 0.83 | 1.05 |
| 11-23 12:07 | +5 | BNB | DOWN | 0.70 | 0.83 | 1.05 |
| 11-23 12:06 | +10 stop | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 11-23 12:06 | +20 | XRP | DOWN | 0.65 | 0.91 | 2.37 |
| 11-23 12:06 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 11-23 12:06 | +10 | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 11-23 12:06 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 11-23 12:06 | +10 stop | HYPE | UP | 0.59 | 0.41 | -2.14 |
| 11-23 12:06 | +10 stop | SOL | UP | 0.64 | 0.47 | -2.05 |
| 11-23 12:06 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 11-23 12:06 | +20 | BTC | DOWN | 0.59 | 0.91 | 2.96 |
| 11-23 12:06 | +15 | BTC | DOWN | 0.59 | 0.78 | 1.60 |
| 11-23 12:06 | +10 | BTC | DOWN | 0.59 | 0.69 | 0.68 |
