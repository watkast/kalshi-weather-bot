# Range-Scalp Bot

*Updated Mon Nov 23 01:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69394 | 60548 | 8846 (146) | 0 | $-18696.55 | -4.3% |
| **+10¢** | 51783 | 41448 | 10335 (189) | 1 | $-17394.76 | -5.3% |
| **+15¢** | 43394 | 32261 | 11133 (244) | 1 | $-15546.03 | -5.7% |
| **+20¢** | 38647 | 26943 | 11704 (306) | 1 | $-13842.17 | -5.7% |
| **+10¢ (15¢ stop)** | 84489 | 84299 | 190 (118) | 1 | $-31060.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 01:45 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 11-23 01:45 | +20 | BTC | DOWN | 0.62 | open |  |
| 11-23 01:45 | +15 | BTC | DOWN | 0.62 | open |  |
| 11-23 01:45 | +10 | BTC | DOWN | 0.62 | open |  |
| 11-23 01:45 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-23 01:43 | +10 stop | BTC | UP | 0.44 | 0.68 | 2.06 |
| 11-23 01:43 | +20 | BTC | UP | 0.45 | 0.68 | 1.96 |
| 11-23 01:43 | +15 | BTC | UP | 0.53 | 0.68 | 1.16 |
| 11-23 01:43 | +10 | BTC | UP | 0.62 | no | -6.37 |
| 11-23 01:43 | +5 | BTC | UP | 0.64 | no | -6.57 |
| 11-23 01:43 | +10 stop | NEAR | DOWN | 0.64 | 0.78 | 1.10 |
| 11-23 01:43 | +20 | NEAR | DOWN | 0.66 | 0.96 | 2.85 |
| 11-23 01:43 | +15 | NEAR | DOWN | 0.66 | 0.96 | 2.85 |
| 11-23 01:43 | +10 | NEAR | DOWN | 0.60 | 0.78 | 1.46 |
| 11-23 01:43 | +5 | NEAR | DOWN | 0.60 | 0.78 | 1.49 |
| 11-23 01:43 | +10 stop | ETH | UP | 0.51 | 0.16 | -3.78 |
| 11-23 01:43 | +10 | ETH | UP | 0.51 | no | -5.28 |
| 11-23 01:43 | +5 | ETH | UP | 0.51 | no | -5.28 |
| 11-23 01:42 | +5 | HYPE | UP | 0.50 | 0.65 | 1.16 |
| 11-23 01:42 | +15 | SOL | UP | 0.55 | 0.77 | 1.89 |
| 11-23 01:41 | +10 stop | HYPE | UP | 0.53 | 0.65 | 0.89 |
| 11-23 01:41 | +10 stop | SOL | UP | 0.60 | 0.77 | 1.40 |
| 11-23 01:41 | +10 | SOL | UP | 0.61 | 0.77 | 1.30 |
| 11-23 01:41 | +5 | SOL | UP | 0.62 | 0.77 | 1.20 |
| 11-23 01:41 | +10 stop | BNB | UP | 0.55 | 0.67 | 0.86 |
| 11-23 01:41 | +10 | BNB | UP | 0.53 | 0.67 | 1.06 |
| 11-23 01:41 | +5 | BNB | UP | 0.53 | 0.67 | 1.06 |
| 11-23 01:41 | +10 stop | BNB | DOWN | 0.40 | 0.52 | 0.85 |
| 11-23 01:41 | +10 | BNB | DOWN | 0.41 | 0.52 | 0.75 |
| 11-23 01:41 | +5 | BNB | DOWN | 0.41 | 0.52 | 0.75 |
| 11-23 01:40 | +10 stop | NEAR | DOWN | 0.67 | 0.45 | -2.54 |
| 11-23 01:40 | +5 | SOL | DOWN | 0.66 | 0.75 | 0.60 |
| 11-23 01:39 | +10 stop | DOGE | UP | 0.55 | 0.69 | 1.07 |
| 11-23 01:39 | +10 | DOGE | UP | 0.56 | 0.69 | 0.97 |
| 11-23 01:39 | +5 | DOGE | UP | 0.55 | 0.69 | 1.07 |
| 11-23 01:39 | +5 | NEAR | UP | 0.57 | 0.66 | 0.56 |
| 11-23 01:39 | +10 stop | ETH | DOWN | 0.64 | 0.83 | 1.63 |
| 11-23 01:39 | +10 | ETH | DOWN | 0.65 | 0.83 | 1.54 |
| 11-23 01:39 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 11-23 01:39 | +10 stop | BTC | DOWN | 0.47 | 0.63 | 1.25 |
