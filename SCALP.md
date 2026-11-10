# Range-Scalp Bot

*Updated Tue Nov 10 04:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54203 | 47289 | 6914 (89) | 3 | $-14719.04 | -4.3% |
| **+10¢** | 40494 | 32425 | 8069 (117) | 3 | $-13669.38 | -5.4% |
| **+15¢** | 33937 | 25240 | 8697 (150) | 4 | $-12419.87 | -5.8% |
| **+20¢** | 30217 | 21094 | 9123 (198) | 5 | $-10823.79 | -5.7% |
| **+10¢ (15¢ stop)** | 66029 | 65919 | 110 (66) | 0 | $-24408.00 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 04:35 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-10 04:35 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-10 04:35 | +5 | BTC | DOWN | 0.66 | 0.73 | 0.40 |
| 11-10 04:34 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-10 04:34 | +10 | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-10 04:34 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 11-10 04:34 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-10 04:33 | +5 | DOGE | UP | 0.69 | open |  |
| 11-10 04:33 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-10 04:33 | +20 | HYPE | DOWN | 0.71 | 0.91 | 1.79 |
| 11-10 04:33 | +15 | HYPE | DOWN | 0.71 | 0.90 | 1.69 |
| 11-10 04:33 | +10 | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-10 04:33 | +5 | HYPE | DOWN | 0.71 | 0.77 | 0.32 |
| 11-10 04:32 | +5 | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 11-10 04:32 | +10 stop | XRP | DOWN | 0.60 | 0.75 | 1.19 |
| 11-10 04:32 | +20 | XRP | DOWN | 0.60 | 0.83 | 2.03 |
| 11-10 04:32 | +15 | XRP | DOWN | 0.60 | 0.75 | 1.19 |
| 11-10 04:32 | +10 | XRP | DOWN | 0.60 | 0.75 | 1.19 |
| 11-10 04:32 | +5 | XRP | DOWN | 0.60 | 0.66 | 0.27 |
| 11-10 04:31 | +10 stop | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 11-10 04:31 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 04:31 | +20 | ETH | DOWN | 0.65 | 0.92 | 2.48 |
| 11-10 04:31 | +15 | ETH | DOWN | 0.65 | 0.82 | 1.43 |
| 11-10 04:31 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 04:31 | +5 | ETH | DOWN | 0.65 | 0.72 | 0.39 |
| 11-10 04:31 | +10 stop | DOGE | UP | 0.68 | 0.50 | -2.14 |
| 11-10 04:31 | +20 | DOGE | UP | 0.68 | open |  |
| 11-10 04:31 | +15 | DOGE | UP | 0.68 | open |  |
| 11-10 04:31 | +10 | DOGE | UP | 0.68 | open |  |
| 11-10 04:31 | +5 | DOGE | UP | 0.68 | 0.77 | 0.61 |
| 11-10 04:31 | +10 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-10 04:31 | +10 stop | NEAR | DOWN | 0.63 | 0.77 | 1.10 |
| 11-10 04:31 | +10 stop | ZEC | DOWN | 0.64 | 0.75 | 0.77 |
| 11-10 04:31 | +15 | ZEC | DOWN | 0.64 | 0.81 | 1.40 |
| 11-10 04:31 | +10 | ZEC | DOWN | 0.64 | 0.75 | 0.77 |
| 11-10 04:31 | +5 | ZEC | DOWN | 0.64 | 0.73 | 0.59 |
| 11-10 04:31 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 04:31 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 04:31 | +5 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 04:31 | +10 stop | ZEC | UP | 0.43 | 0.59 | 1.25 |
