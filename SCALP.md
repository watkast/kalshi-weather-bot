# Range-Scalp Bot

*Updated Tue Nov 24 18:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70886 | 61875 | 9011 (155) | 3 | $-18867.98 | -4.2% |
| **+10¢** | 52871 | 42350 | 10521 (201) | 5 | $-17451.30 | -5.3% |
| **+15¢** | 44286 | 32954 | 11332 (258) | 5 | $-15527.19 | -5.6% |
| **+20¢** | 39433 | 27503 | 11930 (324) | 5 | $-13886.09 | -5.6% |
| **+10¢ (15¢ stop)** | 86300 | 86099 | 201 (121) | 0 | $-31714.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 18:43 | +5 | HYPE | DOWN | 0.61 | 0.70 | 0.57 |
| 11-24 18:42 | +10 stop | ETH | UP | 0.55 | 0.34 | -2.43 |
| 11-24 18:42 | +10 | ETH | UP | 0.54 | open |  |
| 11-24 18:42 | +5 | ETH | UP | 0.52 | open |  |
| 11-24 18:42 | +10 stop | BNB | DOWN | 0.44 | 0.64 | 1.65 |
| 11-24 18:42 | +20 | BNB | DOWN | 0.43 | 0.64 | 1.75 |
| 11-24 18:42 | +15 | BNB | DOWN | 0.43 | 0.64 | 1.75 |
| 11-24 18:42 | +10 | BNB | DOWN | 0.44 | 0.64 | 1.65 |
| 11-24 18:42 | +5 | BNB | DOWN | 0.44 | 0.64 | 1.65 |
| 11-24 18:41 | +10 stop | HYPE | UP | 0.49 | 0.29 | -2.33 |
| 11-24 18:41 | +10 | HYPE | UP | 0.49 | open |  |
| 11-24 18:41 | +5 | HYPE | UP | 0.49 | 0.55 | 0.24 |
| 11-24 18:39 | +10 stop | HYPE | UP | 0.69 | 0.52 | -2.00 |
| 11-24 18:39 | +10 stop | SOL | UP | 0.68 | 0.51 | -2.04 |
| 11-24 18:38 | +10 stop | SOL | DOWN | 0.66 | 0.50 | -1.94 |
| 11-24 18:38 | +5 | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 11-24 18:38 | +10 stop | BTC | UP | 0.65 | 0.76 | 0.81 |
| 11-24 18:38 | +10 | BTC | UP | 0.65 | 0.76 | 0.81 |
| 11-24 18:38 | +5 | BTC | UP | 0.66 | 0.71 | 0.19 |
| 11-24 18:37 | +10 stop | BTC | UP | 0.52 | 0.66 | 1.06 |
| 11-24 18:37 | +10 | BTC | UP | 0.51 | 0.66 | 1.16 |
| 11-24 18:37 | +5 | BTC | UP | 0.51 | 0.66 | 1.16 |
| 11-24 18:37 | +10 stop | DOGE | UP | 0.58 | 0.78 | 1.69 |
| 11-24 18:37 | +10 stop | BNB | UP | 0.60 | 0.73 | 0.99 |
| 11-24 18:37 | +10 stop | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-24 18:36 | +10 stop | ZEC | UP | 0.65 | 0.76 | 0.77 |
| 11-24 18:36 | +5 | SOL | UP | 0.53 | 0.58 | 0.14 |
| 11-24 18:36 | +10 stop | XRP | UP | 0.48 | 0.66 | 1.46 |
| 11-24 18:35 | +10 stop | BNB | UP | 0.57 | 0.40 | -2.05 |
| 11-24 18:35 | +5 | BTC | DOWN | 0.57 | 0.63 | 0.25 |
| 11-24 18:35 | +10 stop | DOGE | UP | 0.45 | 0.60 | 1.15 |
| 11-24 18:34 | +10 stop | HYPE | DOWN | 0.65 | 0.38 | -3.03 |
| 11-24 18:33 | +10 stop | BTC | DOWN | 0.60 | 0.73 | 0.99 |
| 11-24 18:33 | +10 stop | XRP | DOWN | 0.58 | 0.43 | -1.86 |
| 11-24 18:33 | +10 stop | BNB | UP | 0.59 | 0.43 | -1.95 |
| 11-24 18:33 | +15 | BNB | UP | 0.59 | 0.76 | 1.40 |
| 11-24 18:33 | +10 | BNB | UP | 0.59 | 0.73 | 1.09 |
| 11-24 18:33 | +10 stop | ETH | UP | 0.67 | 0.51 | -1.94 |
| 11-24 18:33 | +5 | BNB | UP | 0.65 | 0.73 | 0.50 |
| 11-24 18:32 | +10 stop | XRP | DOWN | 0.65 | 0.50 | -1.84 |
