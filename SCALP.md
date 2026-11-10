# Range-Scalp Bot

*Updated Tue Nov 10 05:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54221 | 47296 | 6925 (89) | 1 | $-14787.08 | -4.3% |
| **+10¢** | 40509 | 32430 | 8079 (117) | 1 | $-13729.88 | -5.4% |
| **+15¢** | 33952 | 25243 | 8709 (150) | 1 | $-12493.15 | -5.9% |
| **+20¢** | 30232 | 21096 | 9136 (198) | 2 | $-10901.98 | -5.8% |
| **+10¢ (15¢ stop)** | 66054 | 65944 | 110 (66) | 0 | $-24427.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 05:02 | +10 stop | BTC | UP | 0.65 | 0.84 | 1.64 |
| 11-10 05:02 | +20 | BTC | UP | 0.65 | 0.86 | 1.85 |
| 11-10 05:02 | +15 | BTC | UP | 0.65 | 0.84 | 1.64 |
| 11-10 05:02 | +10 | BTC | UP | 0.65 | 0.84 | 1.64 |
| 11-10 05:02 | +5 | BTC | UP | 0.65 | 0.84 | 1.64 |
| 11-10 05:01 | +10 stop | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 11-10 05:01 | +20 | ZEC | UP | 0.69 | open |  |
| 11-10 05:01 | +15 | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 11-10 05:01 | +10 | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 11-10 05:01 | +5 | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 11-10 05:01 | +10 stop | ETH | UP | 0.59 | 0.73 | 1.09 |
| 11-10 05:01 | +20 | ETH | UP | 0.59 | 0.82 | 2.02 |
| 11-10 05:01 | +15 | ETH | UP | 0.59 | 0.75 | 1.29 |
| 11-10 05:01 | +10 | ETH | UP | 0.59 | 0.73 | 1.09 |
| 11-10 05:01 | +5 | ETH | UP | 0.59 | 0.65 | 0.27 |
| 11-10 05:00 | +10 stop | BNB | DOWN | 0.56 | 0.28 | -3.18 |
| 11-10 05:00 | +20 | BNB | DOWN | 0.56 | open |  |
| 11-10 05:00 | +15 | BNB | DOWN | 0.56 | open |  |
| 11-10 05:00 | +10 | BNB | DOWN | 0.56 | open |  |
| 11-10 05:00 | +5 | BNB | DOWN | 0.56 | open |  |
| 11-10 04:56 | +10 stop | BNB | UP | 0.59 | 0.72 | 1.01 |
| 11-10 04:55 | +10 stop | BNB | UP | 0.68 | 0.53 | -1.84 |
| 11-10 04:54 | +10 stop | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 11-10 04:53 | +10 stop | ZEC | UP | 0.63 | 0.80 | 1.41 |
| 11-10 04:52 | +10 stop | ETH | DOWN | 0.55 | 0.34 | -2.44 |
| 11-10 04:52 | +10 stop | DOGE | UP | 0.64 | 0.45 | -2.25 |
| 11-10 04:51 | +5 | BTC | DOWN | 0.56 | yes | -5.78 |
| 11-10 04:51 | +10 stop | SOL | UP | 0.67 | 0.84 | 1.44 |
| 11-10 04:50 | +10 stop | BTC | UP | 0.45 | 0.58 | 0.94 |
| 11-10 04:50 | +10 | BTC | UP | 0.45 | 0.58 | 0.94 |
| 11-10 04:50 | +5 | BTC | UP | 0.45 | 0.54 | 0.54 |
| 11-10 04:50 | +10 stop | ETH | UP | 0.66 | 0.45 | -2.44 |
| 11-10 04:49 | +5 | BNB | DOWN | 0.64 | yes | -6.57 |
| 11-10 04:49 | +10 stop | NEAR | UP | 0.59 | 0.83 | 2.13 |
| 11-10 04:48 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-10 04:48 | +10 stop | HYPE | UP | 0.57 | 0.72 | 1.14 |
| 11-10 04:48 | +10 stop | SOL | DOWN | 0.67 | 0.39 | -3.13 |
| 11-10 04:48 | +20 | SOL | DOWN | 0.67 | yes | -6.86 |
| 11-10 04:48 | +15 | SOL | DOWN | 0.67 | yes | -6.86 |
| 11-10 04:48 | +10 | SOL | DOWN | 0.67 | yes | -6.86 |
